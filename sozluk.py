word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap ",
            "BTW": "Başka bir konuya girerken"
            }
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    printt("Bu Kelime bulunamamaktadır.")
