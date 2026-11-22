import pandas as pd

df = pd.read_csv("webtoon_originals_id.csv", sep=",")
print(df.shape)
print(df.head())

print()

#cek kesehatan data
df.info()
print(df.isna().sum())

print()

#cek duplikasi data
print("Jumlah data duplikat:", df.duplicated().sum())

print()

#cek penulisan data
print(df["genre"].value_counts())
print(df["weekdays"].value_counts())
print(df["status"].value_counts())

print()

#cek kolom dengan type float atau int
print(df[["length", "subscribers", "rating", "views", "likes"]].describe())

print()

#telusuri dan perbaiki missing value di kolom authors
print(df.loc[df["authors"].isna(), ["title", "authors"]])
print()
#ketika dilakukan pengecekan manual di webtoon, ditemukan bahwa kedua judul ini di buat oleh author bernama "NA". Namun, karena "NA" termasuk nilai missing bawaan pandas, maka pandas membacanya sebagai NaN. Jadi,nilainya dikembalikan menjadi teks "NA".
df["authors"] = df["authors"].fillna("NA")
print(df.isna().sum())
print(df.loc[df["authors"] == "NA", ["title", "authors"]])

print()

#perbaiki penulisan
teks = ["title", "genre", "authors", "weekdays", "status", "synopsis"]
for col in teks:
    print(col, "whitespace:", (df[col] != df[col].str.strip()).sum())
    df[col] = df[col].str.strip()

print()

#nilai tidak masuk akal pada kolom length, subscribers, rating, views, likes
print("rating = 0:", (df["rating"] == 0).sum(), "dari", len(df))
print("likes > views:", (df["likes"] > df["views"]).sum())
#nilai rating 0 semua, di drop
df = df.drop(columns=["rating"])

print()

#cek akhir data
print("Missing total:", df.isna().sum().sum())
print("Duplikat total:", df.duplicated().sum())
df.info()