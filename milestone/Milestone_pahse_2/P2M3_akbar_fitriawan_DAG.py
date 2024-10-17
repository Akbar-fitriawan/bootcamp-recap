'''
=================================================
Milestone 3

Nama  : Akbar Fitriawan
Batch : FTDS-15-HCK

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset mengenai Real Estate UEA .
=================================================
'''

# Import libraries
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from sqlalchemy import create_engine #koneksi ke postgres
import pandas as pd
from elasticsearch import Elasticsearch


def load_csv_to_postgres():
    '''
    Memuat data dari file CSV ke dalam tabel database PostgreSQL.
    
    Fungsi ini membaca file CSV dan memuat isinya ke dalam tabel PostgreSQL. Detail koneksi
    database telah ditentukan dalam fungsi. Data dari CSV diolah sebagai DataFrame pandas 
    dan kemudian disimpan ke tabel PostgreSQL menggunakan SQLAlchemy.
    '''
 
    database = "airflow_m3"
    username = "airflow_m3"
    password = "airflow_m3"
    host = "postgres"

    # Membuat URL koneksi PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Gunakan URL ini saat membuat koneksi SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()

    df = pd.read_csv('/opt/airflow/dags/P2M3_akbar_fitriawan_data_raw.csv')
    df.to_sql('table_m3', conn, index=False, if_exists='replace') 
    

def ambil_data():
    '''
    Mengambil data dari tabel PostgreSQL dan menyimpannya dalam file CSV.

    Fungsi ini membuka koneksi ke database PostgreSQL menggunakan detail koneksi yang
    telah ditentukan dalam fungsi. Kemudian, data dari tabel bernama 'table_m3' diambil
    dan disimpan dalam sebuah DataFrame pandas. DataFrame tersebut kemudian disimpan 
    sebagai file CSV di lokasi '/opt/airflow/dags/akbar_new_data.csv'.
    '''

    database = "airflow_m3"
    username = "airflow_m3"
    password = "airflow_m3"
    host = "postgres"

    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
    # Gunakan URL ini saat membuat koneksi SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()

    df = pd.read_sql_query("select * from table_m3", conn) # query ambil data dari postgres
    df.to_csv('/opt/airflow/dags/akbar_new_data.csv', sep=',', index=False)
    

def preprocessing():
    ''' 
    Membersihkan data dari duplikat dan mengolah format kolom tertentu.

    Fungsi ini membaca file CSV yang berisi data, membersihkan data dari duplikat, mengubah
    nama kolom menjadi huruf kecil, dan melakukan sejumlah transformasi pada kolom tertentu.
    Data hasil preprocessing disimpan kembali sebagai file CSV.

    Catatan:
    - Data duplikat dihapus.
    - Nama kolom diubah menjadi huruf kecil.
    - Data dengan nilai 'rent' lebih dari nol dipertahankan.
    - Kolom 'purpose' dan 'frequency' dihapus karena hanya memiliki satu kategori.
    - Tanggal diubah menjadi kolom 'posted_month' (bulan) dan 'posted_year' (tahun).
    - Missing value diisi dengan mode untuk kolom bertipe objek dan median untuk kolom bertipe numerik.

    '''
    # pembisihan data
    data = pd.read_csv("/opt/airflow/dags/akbar_new_data.csv")

    # bersihkan data duplikat
    data.drop_duplicates(inplace=True)

    # Rename kolom jadi lowercase
    data.columns = data.columns.str.lower()

    # ambil data yang rent lebih dari nol
    data = data.query('rent>0').copy()


    # Drop columns 'purpose' and 'frequency'
    data.drop(['purpose', 'frequency'], axis=1, inplace=True) # drop data karena hanya 1 kategori dan tidak memberikan informasi bermanfaat valuenya purpose "for rent", frequency "yearly"

    # Extract date year/month/date into new column
    data['posted_date'] = pd.to_datetime(data['posted_date']) # konversi object to datetime

    data['posted_month'] = data['posted_date'].dt.month # buat kolom baru untuk posted month
    data['posted_year'] = data['posted_date'].dt.year # buat kolom baru untuk posted year

    # handling missing value
    for col in data.columns:
        try:
            if data[col].dtype == 'object':
                data[col].fillna(data[col].mode()[0], inplace=True)
            else:
                data[col].fillna(data[col].median(), inplace=True)
        except Exception as e:
            print(f"Error processing column {col}: {e}")

    data.to_csv('/opt/airflow/dags/P2M3_akbar_fitriawan_data_clean.csv', index=False)



    
def upload_to_elasticsearch():
    '''
    Mengunggah data dari file CSV ke Elasticsearch.

    Fungsi ini membaca file CSV yang berisi data yang telah diproses sebelumnya, 
    kemudian mengunggahnya ke Elasticsearch. Setiap baris data diubah menjadi 
    dokumen Elasticsearch dan diindeks ke dalam indeks yang ditentukan.

    Catatan:
    - File CSV yang dibaca sebelumnya telah melalui proses preprocessing.
    - Setiap baris data diubah menjadi dokumen Elasticsearch dan diindeks 
      dengan nomor id yang sesuai dengan indeks baris dalam DataFrame.
    - Indeks yang digunakan dalam Elasticsearch adalah 'table_m3'
    '''

    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv('/opt/airflow/dags/P2M3_akbar_fitriawan_data_clean.csv')
    
    for i, r in df.iterrows():
        doc = r.to_dict()  # Convert the row to a dictionary
        res = es.index(index="table_m3", id=i+1, body=doc)
        print(f"Response from Elasticsearch: {res}")
        

        
default_args = {
    'owner': 'akbar_fitriawan', 
    'start_date': datetime(2023, 12, 24, 12, 00)
}

with DAG(
    "P2M3_akbar_fitriawan_DAG", #atur sesuai nama project kalian
    description='Milestone_3',
    schedule_interval='30 6 * * *', #atur schedule untuk menjalankan airflow pada 06:30.
    default_args=default_args, 
    catchup=False
) as dag:
    # task 1 melakukan load csv ke postgres
    Task : 1
    load_csv_task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres) #sesuaikan dengan nama fungsi yang kalian buat
    
    # task 2 melakukan ambil data dari postgres
    task: 2
    ambil_data_pg = PythonOperator(
        task_id='ambil_data_postgres',
        python_callable=ambil_data) 
    
    # task 3 untuk melakukan menjalankan pembersihan data.
    Task: 3
    edit_data = PythonOperator(
        task_id='edit_data',
        python_callable=preprocessing)

    # Task 4 untuk melakukan upload data ke elastic search
    upload_data = PythonOperator(
        task_id='upload_data_elastic',
        python_callable=upload_to_elasticsearch)

    #proses untuk menjalankan di airflow
    load_csv_task  >> ambil_data_pg >> edit_data  >> upload_data



