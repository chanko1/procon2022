import difflib

import speech_recognition as sr
 
r = sr.Recognizer()
 
with sr.AudioFile("E16.wav") as source:
    audio = r.record(source)
 
text_a = r.recognize_google(audio, language='en-US')

text_E01 = "Olson power of Mount Asama magma stones at on Yoshi"
text_E02 = "one of the most famous hot springs in Japan ikaho Onsen"
text_E03 = "a checkpoint from long ago with Suey pass"
text_E04 = "Lockheed Aluma dolls at the shoe Lindsey"
text_E05 = "which insulin topness please don't do other kind of Jama older"
text_E06 = "joining conto and Chanel to takasaki City"
text_E07 = "percentage over the weaving industry in Japan can you City"
text_E08 = "securing rulers of kisetsu Onsen"
text_E09 = "the capital of grimaced and the City of silk my bocce"
text_E10 = "a leading question Sinker uchimura Kansas"
text_E11 = "when do cherry blossoms and the samba rocks beautiful sight to see"
text_E12 = "bringing back the day won't past the Zucca"
text_E13 = "leading wide receiver does gentle slopes of Mount of a tiger"
text_E14 = "Treasure of Natural Valley National Park"
text_E15 = "everyone dancing has 12 the Yankee bushy Fork song"
text_E16 = "Dynamic waterfalls in Bali"
text_E17 = "two medium working together Boomers people"
text_E18 = "shaped like a flying crane kumartuli picture"
text_E19 = "huel for poor people"
text_E20 = "the longest rivers in canto that toenail River"
text_E21 = "line to cedar trees in unaka reminders of nakasendo"
text_E22 = "Japan's first Soup Factory tomioka silk Mill"
text_E23 = "a successful hard-working from old new modern seal Bala the suitcase"
text_E24 = "leaks and konyaku Local Foods"
text_E25 = "a perfect place to hike and camp Mount Haruna"
text_E26 = "a beautiful spot for a Xavier's hanayama Park"
text_E27 = "giving Comfort to the people candle statue"
text_E28 = "good looking dog blinks good luck at the Moline G Temple"
text_E29 = "a wise Christian educator niijima"
text_E30 = "a great Japanese lighter"
text_E31 = "the top producer of cocoons and silk in Japan"
text_E32 = "wonderful places to ski and climb minakami and panigale"
text_E33 = "telling us about old times. Monument"
text_E34 = "the home of Mason silk is sake City"
text_E35 = "glowing with autumn colors Mountain Miyagi"
text_E36 = "questions of the rearview Lee Canyon"
text_E37 = "suspected sis Asian X shrine"
text_E38 = "healing mind and Bali Shima Onsen"
text_E39 = "thunder on the strong winds dirty and kindness in Gilmer"
text_E40 = "energy from Waller groomers electricity"
text_E41 = "William looping layaway Shimizu"
text_E42 = "Ablaze Samurai leaders in history"
text_E43 = "Pioneer informing to Natsu 10gb"
text_E44 = "the master of Japanese mess say Kiko"

per_1 = difflib.SequenceMatcher(None, text_a, text_E01).ratio()
print("E01  ",per_1)
per_2 = difflib.SequenceMatcher(None, text_a, text_E02).ratio()
print("E02  ",per_2)
per_3 = difflib.SequenceMatcher(None, text_a, text_E03).ratio()
print("E03  ",per_3)
per_4 = difflib.SequenceMatcher(None, text_a, text_E04).ratio()
print("E04  ",per_4)
per_5 = difflib.SequenceMatcher(None, text_a, text_E05).ratio()
print("E05  ",per_5)
per_6 = difflib.SequenceMatcher(None, text_a, text_E06).ratio()
print("E06  ",per_6)
per_7 = difflib.SequenceMatcher(None, text_a, text_E07).ratio()
print("E07  ",per_7)
per_8 = difflib.SequenceMatcher(None, text_a, text_E08).ratio()
print("E08  ",per_8)
per_9 = difflib.SequenceMatcher(None, text_a, text_E09).ratio()
print("E09  ",per_9)
per_10 = difflib.SequenceMatcher(None, text_a, text_E10).ratio()
print("E10  ",per_10)
per_11 = difflib.SequenceMatcher(None, text_a, text_E11).ratio()
print("E11  ",per_11)
per_12 = difflib.SequenceMatcher(None, text_a, text_E12).ratio()
print("E12  ",per_12)
per_13 = difflib.SequenceMatcher(None, text_a, text_E13).ratio()
print("E13  ",per_13)
per_14 = difflib.SequenceMatcher(None, text_a, text_E14).ratio()
print("E14  ",per_14)
per_15 = difflib.SequenceMatcher(None, text_a, text_E15).ratio()
print("E15  ",per_15)
per_16 = difflib.SequenceMatcher(None, text_a, text_E16).ratio()
print("E16  ",per_16)
per_17 = difflib.SequenceMatcher(None, text_a, text_E17).ratio()
print("E17  ",per_17)
per_18 = difflib.SequenceMatcher(None, text_a, text_E18).ratio()
print("E18  ",per_18)
per_19 = difflib.SequenceMatcher(None, text_a, text_E19).ratio()
print("E19  ",per_19)
per_20 = difflib.SequenceMatcher(None, text_a, text_E20).ratio()
print("E20  ",per_20)
per_21 = difflib.SequenceMatcher(None, text_a, text_E21).ratio()
print("E21  ",per_21)
per_22 = difflib.SequenceMatcher(None, text_a, text_E22).ratio()
print("E22  ",per_22)
per_23 = difflib.SequenceMatcher(None, text_a, text_E23).ratio()
print("E23  ",per_23)
per_24 = difflib.SequenceMatcher(None, text_a, text_E24).ratio()
print("E24  ",per_24)
per_25 = difflib.SequenceMatcher(None, text_a, text_E25).ratio()
print("E25  ",per_25)
per_26 = difflib.SequenceMatcher(None, text_a, text_E26).ratio()
print("E26  ",per_26)
per_27 = difflib.SequenceMatcher(None, text_a, text_E27).ratio()
print("E27  ",per_27)
per_28 = difflib.SequenceMatcher(None, text_a, text_E28).ratio()
print("E28  ",per_28)
per_29 = difflib.SequenceMatcher(None, text_a, text_E29).ratio()
print("E29  ",per_29)
per_30 = difflib.SequenceMatcher(None, text_a, text_E30).ratio()
print("E30  ",per_30)
per_31 = difflib.SequenceMatcher(None, text_a, text_E31).ratio()
print("E31  ",per_31)
per_32 = difflib.SequenceMatcher(None, text_a, text_E32).ratio()
print("E32  ",per_32)
per_33 = difflib.SequenceMatcher(None, text_a, text_E33).ratio()
print("E33  ",per_33)
per_34 = difflib.SequenceMatcher(None, text_a, text_E34).ratio()
print("E34  ",per_34)
per_35 = difflib.SequenceMatcher(None, text_a, text_E35).ratio()
print("E35  ",per_35)
per_36 = difflib.SequenceMatcher(None, text_a, text_E36).ratio()
print("E36  ",per_36)
per_37 = difflib.SequenceMatcher(None, text_a, text_E37).ratio()
print("E37  ",per_37)
per_38 = difflib.SequenceMatcher(None, text_a, text_E38).ratio()
print("E38  ",per_38)
per_39 = difflib.SequenceMatcher(None, text_a, text_E39).ratio()
print("E39  ",per_39)
per_40 = difflib.SequenceMatcher(None, text_a, text_E40).ratio()
print("E40  ",per_40)
per_41 = difflib.SequenceMatcher(None, text_a, text_E41).ratio()
print("E41  ",per_41)
per_42 = difflib.SequenceMatcher(None, text_a, text_E42).ratio()
print("E42  ",per_42)
per_43 = difflib.SequenceMatcher(None, text_a, text_E43).ratio()
print("E43  ",per_43)
per_44 = difflib.SequenceMatcher(None, text_a, text_E44).ratio()
print("E44  ",per_44)


per_all = [per_1,per_2,per_3,per_4,per_5,per_6,per_7,per_8,per_9,per_10,
per_11,per_12,per_13,per_14,per_15,per_16,per_17,per_18,per_19,per_20,
per_21,per_22,per_23,per_24,per_25,per_26,per_27,per_28,per_29,per_30,
per_31,per_32,per_33,per_34,per_35,per_36,per_37,per_38,per_39,per_40,
per_41,per_42,per_43,per_44]

print(max(per_all))
per_max = max(per_all)
count = 0

for per_max_name in per_all:
    count = count + 1
    if per_max_name == per_max:
        print("E",count)