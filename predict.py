import joblib
import pandas as pd
import os

def main():
    # minta user masukkan nama file csv yang berisi data yang perlu diprediksi status attrition-nya
    input_file = input("Masukkan nama file CSV (misalnya df_attrition_unlabeled.csv): ").strip()

    # cek apakah file ada
    if not os.path.exists(input_file):
        print(f"❌ File '{input_file}' tidak ditemukan.")
        return

    # load model
    try:
        model = joblib.load('model.pkl')
    except FileNotFoundError:
        print("❌ File model 'model.pkl' tidak ditemukan.")
        return

    # load data
    try:
        new_data = pd.read_csv(input_file)
    except Exception as e:
        print(f"❌ Gagal membaca file CSV: {e}")
        return

    # hapus kolom 'Attrition' jika ada
    if 'Attrition' in new_data.columns:
        new_data = new_data.drop('Attrition', axis=1)

    # prediksi
    try:
        prediksi = model.predict(new_data)
        new_data['Predicted_Attrition'] = prediksi
    except Exception as e:
        print(f"❌ Gagal memproses prediksi: {e}")
        return

    # simpan hasil
    output_file = 'hasil_prediksi_attrition.csv'
    new_data.to_csv(output_file, index=False)
    print(f"✅ Prediksi berhasil disimpan di: {output_file}")

if __name__ == '__main__':
    main()
