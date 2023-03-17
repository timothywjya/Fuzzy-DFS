from fuzzywuzzy import fuzz
import panda as pd

#ratio itu hasil harus sama semua
ratio = fuzz.ratio("Nama Saya Adrian", "nama saya adrian")
print("Hasil dari ratio adalah = ", ratio)

ratio = fuzz.ratio("Nama Saya Adrian", "Nama Saya Adrian")
print("Hasil dari ratio adalah = ", ratio)

ratio = fuzz.ratio("Nama Saya Adrian", "ZZZZZZZZZZZ")
print("Hasil dari ratio adalah = ", ratio)

ratio = fuzz.ratio("Nama Saya Adrian", "za")
print("Hasil dari ratio adalah = ", ratio)

#partial_ratio membandingkan
partial_ratio = fuzz.partial_ratio("Nama Saya Adrian", "nama saya adrian")
print("Hasil dari partial ratio adalah ",partial_ratio)

partial_ratio = fuzz.partial_ratio("Nama Saya Adrian", "Nama Saya Adrian")
print("Hasil dari ratio adalah = ", partial_ratio)

partial_ratio = fuzz.partial_ratio("Nama Saya Adrian", "ZZZZZZZZZZZ")
print("Hasil dari ratio adalah = ", partial_ratio)

partial_ratio = fuzz.partial_ratio("Nama Saya Adrian", "za")
print("Hasil dari ratio adalah = ", partial_ratio)

#token_ratio tidak peduli besar kecil 
a = fuzz.token_set_ratio("Nama Saya Adrian", "nama saya adrian")
print("Hasil dari token ratio adalah ",a)

a = fuzz.token_set_ratio("Nama Saya Adrian", "Nama Saya Adrian")
print("Hasil dari token ratio adalah = ", a)

a = fuzz.token_set_ratio("Nama Saya Adrian", "ZZZZZZZZZZZ")
print("Hasil dari token ratio adalah = ", a)

a = fuzz.token_set_ratio("Nama Saya Adrian", "za")
print("Hasil dari token ratio adalah = ", a)

b = fuzz.partial_token_set_ratio("Nama Saya Adrian", "nama saya adrian")
print("Hasil dari partial token ratio adalah ",b)

b = fuzz.partial_token_set_ratio("Nama Saya Adrian", "Nama Saya Adrian")
print("Hasil dari partial token ratio adalah = ", b)

b = fuzz.partial_token_set_ratio("Nama Saya Adrian", "ZZZZZZZZZZZ")
print("Hasil dari partial token ratio adalah = ", b)

b = fuzz.partial_token_set_ratio("Nama Saya Adrian", "za")
print("Hasil dari partial token ratio adalah = ", b)

