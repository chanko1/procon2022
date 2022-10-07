import difflib

import speech_recognition as sr
 
r = sr.Recognizer()
 
with sr.AudioFile("J27.wav") as source:
    audio = r.record(source)
 
text_a = r.recognize_google(audio, language='ja-JP')

text_J01 = "アサマノ イタズラ 鬼の押し出し"
text_J02 = "伊香保温泉 日本の名湯"
text_J03 = "碓氷峠の関所跡"
text_J04 = "縁起だるまの少林山"
text_J05 = "太田金山子育て呑龍"
text_J06 = "関東と信越つなぐ高崎市"
text_J07 = "桐生は日本の旗 どころ"
text_J08 = "草 強いとこ 薬のいで湯"
text_J09 = "銭湯 前橋 糸の町"
text_J10 = "心の灯台 内村鑑三"
text_J11 = "三波石と共に名高い 冬桜"
text_J12 = "しのぶ毛の国 双子塚"
text_J13 = "裾野は長し赤城山"
text_J14 = "仙境 尾瀬沼 花の原"
text_J15 = "そろいの支度で八木節音頭"
text_J16 = "滝は吹割片品渓谷"
text_J17 = "力を合わせる 200万"
text_J18 = "鶴舞う形の群馬県"
text_J19 = "戦火の鬼神 茂左衛門"
text_J20 = "利根は坂東一の川"
text_J21 = "中山道 しのぶ 安中杉並木"
text_J22 = "日本で最初の富岡製糸"
text_J23 = "沼田城下の塩原太助"
text_J24 = "ねぎとこんにゃく 下仁田 名産"
text_J25 = "登る榛名のキャンプ村"
text_J26 = "花山公園つつじの名所"
text_J27 = "白衣観音 じひのみて"
text_J28 = "分福茶釜の茂林寺"
text_J29 = "平和の使い 新島襄"
text_J30 = "誇る文豪 田山花袋"
text_J31 = "まゆと生糸は日本一"
text_J32 = "水上 谷川 スキーと登山"
text_J33 = "昔を語る多胡の古碑"
text_J34 = "銘仙織 出す 伊勢崎市"
text_J35 = "もみじに映える 妙義山"
text_J36 = "耶馬渓 しのぐ 吾妻峡"
text_J37 = "縁は 古市 貫前神社"
text_J38 = "よのちり洗う四万温泉"
text_J39 = "ライトを空っ風義理人情"
text_J40 = "理想の電化に電源群馬"
text_J41 = "ループで名高い清水トンネル"
text_J42 = "歴史に名高い 新田義貞"
text_J43 = "老農船津伝次平"
text_J44 = "和算の大家 赤黄は"

per_1 = difflib.SequenceMatcher(None, text_a, text_J01).ratio()
print("J01  ",per_1)
per_2 = difflib.SequenceMatcher(None, text_a, text_J02).ratio()
print("J02  ",per_2)
per_3 = difflib.SequenceMatcher(None, text_a, text_J03).ratio()
print("J03  ",per_3)
per_4 = difflib.SequenceMatcher(None, text_a, text_J04).ratio()
print("J04  ",per_4)
per_5 = difflib.SequenceMatcher(None, text_a, text_J05).ratio()
print("J05  ",per_5)
per_6 = difflib.SequenceMatcher(None, text_a, text_J06).ratio()
print("J06  ",per_6)
per_7 = difflib.SequenceMatcher(None, text_a, text_J07).ratio()
print("J07  ",per_7)
per_8 = difflib.SequenceMatcher(None, text_a, text_J08).ratio()
print("J08  ",per_8)
per_9 = difflib.SequenceMatcher(None, text_a, text_J09).ratio()
print("J09  ",per_9)
per_10 = difflib.SequenceMatcher(None, text_a, text_J10).ratio()
print("J10  ",per_10)
per_11 = difflib.SequenceMatcher(None, text_a, text_J11).ratio()
print("J11  ",per_11)
per_12 = difflib.SequenceMatcher(None, text_a, text_J12).ratio()
print("J12  ",per_12)
per_13 = difflib.SequenceMatcher(None, text_a, text_J13).ratio()
print("J13  ",per_13)
per_14 = difflib.SequenceMatcher(None, text_a, text_J14).ratio()
print("J14  ",per_14)
per_15 = difflib.SequenceMatcher(None, text_a, text_J15).ratio()
print("J15  ",per_15)
per_16 = difflib.SequenceMatcher(None, text_a, text_J16).ratio()
print("J16  ",per_16)
per_17 = difflib.SequenceMatcher(None, text_a, text_J17).ratio()
print("J17  ",per_17)
per_18 = difflib.SequenceMatcher(None, text_a, text_J18).ratio()
print("J18  ",per_18)
per_19 = difflib.SequenceMatcher(None, text_a, text_J19).ratio()
print("J19  ",per_19)
per_20 = difflib.SequenceMatcher(None, text_a, text_J20).ratio()
print("J20  ",per_20)
per_21 = difflib.SequenceMatcher(None, text_a, text_J21).ratio()
print("J21  ",per_21)
per_22 = difflib.SequenceMatcher(None, text_a, text_J22).ratio()
print("J22  ",per_22)
per_23 = difflib.SequenceMatcher(None, text_a, text_J23).ratio()
print("J23  ",per_23)
per_24 = difflib.SequenceMatcher(None, text_a, text_J24).ratio()
print("J24  ",per_24)
per_25 = difflib.SequenceMatcher(None, text_a, text_J25).ratio()
print("J25  ",per_25)
per_26 = difflib.SequenceMatcher(None, text_a, text_J26).ratio()
print("J26  ",per_26)
per_27 = difflib.SequenceMatcher(None, text_a, text_J27).ratio()
print("J27  ",per_27)
per_28 = difflib.SequenceMatcher(None, text_a, text_J28).ratio()
print("J28  ",per_28)
per_29 = difflib.SequenceMatcher(None, text_a, text_J29).ratio()
print("J29  ",per_29)
per_30 = difflib.SequenceMatcher(None, text_a, text_J30).ratio()
print("J30  ",per_30)
per_31 = difflib.SequenceMatcher(None, text_a, text_J31).ratio()
print("J31  ",per_31)
per_32 = difflib.SequenceMatcher(None, text_a, text_J32).ratio()
print("J32  ",per_32)
per_33 = difflib.SequenceMatcher(None, text_a, text_J33).ratio()
print("J33  ",per_33)
per_34 = difflib.SequenceMatcher(None, text_a, text_J34).ratio()
print("J34  ",per_34)
per_35 = difflib.SequenceMatcher(None, text_a, text_J35).ratio()
print("J35  ",per_35)
per_36 = difflib.SequenceMatcher(None, text_a, text_J36).ratio()
print("J36  ",per_36)
per_37 = difflib.SequenceMatcher(None, text_a, text_J37).ratio()
print("J37  ",per_37)
per_38 = difflib.SequenceMatcher(None, text_a, text_J38).ratio()
print("J38  ",per_38)
per_39 = difflib.SequenceMatcher(None, text_a, text_J39).ratio()
print("J39  ",per_39)
per_40 = difflib.SequenceMatcher(None, text_a, text_J40).ratio()
print("J40  ",per_40)
per_41 = difflib.SequenceMatcher(None, text_a, text_J41).ratio()
print("J41  ",per_41)
per_42 = difflib.SequenceMatcher(None, text_a, text_J42).ratio()
print("J42  ",per_42)
per_43 = difflib.SequenceMatcher(None, text_a, text_J43).ratio()
print("J43  ",per_43)
per_44 = difflib.SequenceMatcher(None, text_a, text_J44).ratio()
print("J44  ",per_44)


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
        print("J",count)