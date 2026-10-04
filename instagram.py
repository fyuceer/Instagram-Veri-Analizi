import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from matplotlib.widgets import Button


# =========================================================
# VERİ SETİNİ OKUMA
# =========================================================

data = pd.read_csv("Instagram data.csv", encoding="Latin1")


# =========================================================
# SAYFA 1 - FROM HOME
# =========================================================

def analiz_1(fig):
    fig.clear()

    ax = fig.add_subplot(111)

    ax.hist(data["From Home"], bins=20)

    ax.set_title("Ana Sayfadan Gelen Erişim")
    ax.set_xlabel("From Home")
    ax.set_ylabel("Frekans")

    fig.suptitle("Instagram Veri Analizi - 1 / 9", fontsize=14)

    fig.subplots_adjust(bottom=0.15)


# =========================================================
# SAYFA 2 - FROM HASHTAGS
# =========================================================

def analiz_2(fig):
    fig.clear()

    ax = fig.add_subplot(111)

    ax.hist(data["From Hashtags"], bins=20)

    ax.set_title("Hashtaglerden Gelen Erişim")
    ax.set_xlabel("From Hashtags")
    ax.set_ylabel("Frekans")

    fig.suptitle("Instagram Veri Analizi - 2 / 9", fontsize=14)

    fig.subplots_adjust(bottom=0.15)


# =========================================================
# SAYFA 3 - FROM EXPLORE
# =========================================================

def analiz_3(fig):
    fig.clear()

    ax = fig.add_subplot(111)

    ax.hist(data["From Explore"], bins=20)

    ax.set_title("Keşfetten Gelen Erişim")
    ax.set_xlabel("From Explore")
    ax.set_ylabel("Frekans")

    fig.suptitle("Instagram Veri Analizi - 3 / 9", fontsize=14)

    fig.subplots_adjust(bottom=0.15)


# =========================================================
# SAYFA 4 - ERİŞİM KAYNAKLARI PIE CHART
# =========================================================

def analiz_4(fig):
    fig.clear()

    kaynaklar = [
        data["From Home"].sum(),
        data["From Hashtags"].sum(),
        data["From Explore"].sum(),
        data["From Other"].sum()
    ]

    etiketler = [
        "From Home",
        "From Hashtags",
        "From Explore",
        "From Other"
    ]

    ax = fig.add_subplot(111)

    ax.pie(
        kaynaklar,
        labels=etiketler,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Erişim Kaynaklarının Dağılımı")

    fig.suptitle("Instagram Veri Analizi - 4 / 9", fontsize=14)

    fig.subplots_adjust(bottom=0.15)


# =========================================================
# SAYFA 5 - WORD CLOUD
# =========================================================

def analiz_5(fig):
    fig.clear()

    # Caption
    captions = data["Caption"].dropna().astype(str)

    caption_text = " ".join(captions)

    wordcloud_caption = WordCloud(
        width=600,
        height=400,
        background_color="white"
    ).generate(caption_text)

    # Hashtags
    hashtags = data["Hashtags"].dropna().astype(str)

    hashtag_text = " ".join(hashtags)

    wordcloud_hashtag = WordCloud(
        width=600,
        height=400,
        background_color="white"
    ).generate(hashtag_text)

    # Sol grafik
    ax1 = fig.add_subplot(1, 2, 1)

    ax1.imshow(
        wordcloud_caption,
        interpolation="bilinear"
    )

    ax1.axis("off")
    ax1.set_title("Caption Kelimeleri")

    # Sağ grafik
    ax2 = fig.add_subplot(1, 2, 2)

    ax2.imshow(
        wordcloud_hashtag,
        interpolation="bilinear"
    )

    ax2.axis("off")
    ax2.set_title("Hashtag Kelimeleri")

    fig.suptitle(
        "Instagram Veri Analizi - 5 / 9",
        fontsize=14
    )

    fig.subplots_adjust(
        bottom=0.15,
        wspace=0.1
    )


# =========================================================
# SAYFA 6 - SCATTER PLOT ANALİZLERİ
# =========================================================

def analiz_6(fig):
    fig.clear()

    # 1. Likes - Impressions
    ax1 = fig.add_subplot(1, 3, 1)

    ax1.scatter(
        data["Likes"],
        data["Impressions"]
    )

    ax1.set_title("Likes - Impressions")
    ax1.set_xlabel("Likes")
    ax1.set_ylabel("Impressions")

    # 2. Profile Visits - Comments
    ax2 = fig.add_subplot(1, 3, 2)

    ax2.scatter(
        data["Profile Visits"],
        data["Comments"]
    )

    ax2.set_title("Profile Visits - Comments")
    ax2.set_xlabel("Profile Visits")
    ax2.set_ylabel("Comments")

    # 3. Shares - Impressions
    ax3 = fig.add_subplot(1, 3, 3)

    ax3.scatter(
        data["Shares"],
        data["Impressions"]
    )

    ax3.set_title("Shares - Impressions")
    ax3.set_xlabel("Shares")
    ax3.set_ylabel("Impressions")

    fig.suptitle(
        "Instagram Veri Analizi - 6 / 9",
        fontsize=14
    )

    fig.subplots_adjust(
        bottom=0.18,
        wspace=0.4
    )


# =========================================================
# SAYFA 7 - KORELASYON ANALİZİ
# =========================================================

def analiz_7(fig):
    fig.clear()

    numeric_data = data.select_dtypes(
        include=["number"]
    )

    correlation = numeric_data.corr()

    ax = fig.add_subplot(111)

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )

    ax.set_title("Korelasyon Matrisi")

    fig.suptitle(
        "Instagram Veri Analizi - 7 / 9",
        fontsize=14
    )

    fig.subplots_adjust(
        bottom=0.15
    )


# =========================================================
# SAYFA 8 - FOLLOW CONVERSION RATE
# =========================================================

def analiz_8(fig):
    fig.clear()

    profile_visits = data["Profile Visits"].replace(0, pd.NA)

    conversion_rate = (
        data["Follows"] /
        profile_visits
    ) * 100

    ax = fig.add_subplot(111)

    ax.plot(
        conversion_rate,
        marker="o"
    )

    ax.set_title(
        "Profil Ziyaretlerinden Takipçiye Dönüşüm Oranı"
    )

    ax.set_xlabel("Gönderi")
    ax.set_ylabel("Dönüşüm Oranı (%)")

    ax.grid(True)

    fig.suptitle(
        "Instagram Veri Analizi - 8 / 9",
        fontsize=14
    )

    fig.subplots_adjust(
        bottom=0.15
    )


# =========================================================
# SAYFA 9 - PROFILE VISITS / FOLLOWS
# =========================================================

def analiz_9(fig):
    fig.clear()

    ax = fig.add_subplot(111)

    ax.scatter(
        data["Profile Visits"],
        data["Follows"]
    )

    ax.set_title(
        "Profil Ziyaretleri ve Takipçi Kazanımı"
    )

    ax.set_xlabel("Profile Visits")
    ax.set_ylabel("Follows")

    fig.suptitle(
        "Instagram Veri Analizi - 9 / 9",
        fontsize=14
    )

    fig.subplots_adjust(bottom=0.15)


# =========================================================
# TÜM ANALİZ FONKSİYONLARI
# =========================================================

analizler = [
    analiz_1,
    analiz_2,
    analiz_3,
    analiz_4,
    analiz_5,
    analiz_6,
    analiz_7,
    analiz_8,
    analiz_9
]


# =========================================================
# SAYFA GEÇİŞ SİSTEMİ
# =========================================================

fig = plt.figure(figsize=(12, 7))

mevcut_sayfa = 0


def sayfayi_goster():
    
    analizler[mevcut_sayfa](fig)

    # Önceki butonu
    ax_onceki = fig.add_axes(
        [0.15, 0.02, 0.20, 0.06]
    )

    buton_onceki = Button(
        ax_onceki,
        "Önceki"
    )

    # Sonraki butonu
    ax_sonraki = fig.add_axes(
        [0.65, 0.02, 0.20, 0.06]
    )

    buton_sonraki = Button(
        ax_sonraki,
        "Sonraki"
    )

    # Butonları saklıyoruz.
    fig.buton_onceki = buton_onceki
    fig.buton_sonraki = buton_sonraki

    # Buton olayları
    buton_onceki.on_clicked(onceki_sayfa)
    buton_sonraki.on_clicked(sonraki_sayfa)

    fig.canvas.draw_idle()


def onceki_sayfa(event):
    global mevcut_sayfa

    if mevcut_sayfa > 0:
        mevcut_sayfa -= 1

    sayfayi_goster()


def sonraki_sayfa(event):
    global mevcut_sayfa

    if mevcut_sayfa < len(analizler) - 1:
        mevcut_sayfa += 1

    sayfayi_goster()


# İlk sayfayı göster
sayfayi_goster()


plt.show()