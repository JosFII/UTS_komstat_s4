import streamlit as st
import base64
import pandas as pd
st.markdown(
'''
<style>
    .stApp {
   background-color: white;
    }
 
       .stWrite,.stMarkdown,.stTextInput,h1, h2, h3, h4, h5, h6 {
            color: purple !important;
        }
</style>
''',
unsafe_allow_html=True
)
st.title("Monte Carlo Simulation, Markov Chain, and Hidden Markov Model")
st.write("""dibuat oleh  
         nama: Joseph FIlius H  
         NIM: 20234920002""")
st.header("Flowchart")
st.image("flowchart.jpg")
st.header("Data: data tangan poker dari 1jt permainan")
st.write("data berisi data tangan poker texas holdem dari 1jt permainan, data akan digunakan untuk simulasi monte carlo")
st.write("sumber data: https://www.kaggle.com/datasets/joogollucci/poker-hands-dataset")
st.image("pokdata.png")

st.write("karena file data tangan poker terlalu besar untuk diupload ke git hub maka tadi digantikan gambar dari sebagian data")
st.write("""penjelasan variabel  
         - hand: kartu yang berada ditangan  
         - flop: kondisi tangan dealer saat 3 kartu kebuka  
         - result1: kombinasi terbagus yang dihasilkan tangan saat flop  
         - turn kondisi tangan dealer saat 4 kartu kebuka  
         - result2: kombinasi terbagus yang dihasilkan tangan saat turn  
         - river: kondisi tangan dealer saat 5 kartu kebuka  
         - result3: kombinasi terbagus yang dihasilkan tangan saat river  """)

st.markdown(""" untuk markov chain dan hidden markov model akan digunakan data stok bca tahun 2024  
            data diambil dengan kode R berikut \n
            library(tidyquant)
            library(quantmod)
            options("getSymbols.warning4.0"=FALSE)
            options("getSymbols.yahoo.warning"=FALSE)
            getSymbols('BBCA.JK',from = '2024-01-01',
           to = "2024-12-31")
""")
df4=pd.read_csv("bca.csv")
df4
st.write("""penjelasan variabel  
         - BBCA.JK.open: harga BBCA.JK saat open  
         - BBCA.JK.high: harga BBCA.JK saat tertinggi  
         - BBCA.JK.low: harga BBCA.JK saat terlendah   
         - BBCA.JK.close: harga BBCA.JK saat tutup   
         - BBCA.JK.volume: jumlah stok bca  
         - BBCA.JK.adjusted: harga BBCA.JK jika sudah di adjust   
         """)


st.subheader("Data Exploration")
st.image("pokdata.png")
st.markdown("""Berikut kode untuk barchart dari hasil tangan pada result 3 \n
            library(ggplot2)
            pok=read.csv("poker_dataset.csv")
            ggplot(pok,aes(x=result3))+
                geom_bar()""")
st.image("graph_data.png")
st.write("berikut total tangan yang terbuat pada result 3")
df2=pd.read_csv("datanum.csv")
df2

df4
st.write("berikut summary dari data stok bca")
st.write(df4.describe())
st.markdown("""berikut histogram harga BBCA.JJK.adjusted \n
            ggplot(aes(x=BBCA.JK.Adjusted),data=BBCA.JK)+
              geom_histogram(fill="red",color="black")+
              labs(title = "histogram harga BBCA.JK.Adjusted")
""")
st.image("bcahis.png")

st.subheader("Feature Engineering")
st.markdown("""pertama kita akan menghitung return harian dari stok bca \n
            bca_log <- dailyReturn(BBCA.JK,type = 'log')""")
st.markdown("""berikut grafik dari return harian stok bca \n
            ggplot(df5, aes(date, daily.returns)) + geom_line() + scale_x_date('Month/2017')  + ylab("bca Log Daily Return") +
            xlab("") + labs(title = "bca Daily Return (Log)")
""")
st.image("bcaret.png")
st.markdown("""terus kita harus mengecek normalitas dari return stok bca \n
            shapiro.test(as.vector(bca_log))
""")
st.image("shap.png")
st.write("karena p value > 5%, maka return stok bca berdistribusi normal")

st.subheader("Monte Carlo Simulation")
st.markdown("""untuk melakukan simulasi monte carlo pertama kita perlu mencari probabilitas terjadinya suatu tangan pada result3, 
            berikut kode di R nya \n
            FL=0
            FOA=0
            FH=0
            NO=0
            P=0
            RF=0
            ST=0
            STF=0
            TOA=0
            TP=0
            
            for(x in 1:length(pok[,7])){
              if(pok[x,7]=="FLUSH"){
                FL=FL+1
              } else if(pok[x,7]=="FOUR OF A KIND"){
                FOA=FOA+1
              } else if(pok[x,7]=="FULL HOUSE"){
                FH=FH+1
              } else if(pok[x,7]=="NOTHING"){
                NO=NO+1
              }else if(pok[x,7]=="PAIR"){
                P=P+1
              }else if(pok[x,7]=="ROYAL FLUSH"){
                RF=RF+1
              }else if(pok[x,7]=="STRAIGHT"){
                ST=ST+1
              }else if(pok[x,7]=="STRAIGHT FLUSH"){
                STF=STF+1
              }else if(pok[x,7]=="THREE OF A KIND"){
                TOA=TOA+1
              }else if(pok[x,7]=="TWO PAIR"){
                TP=TP+1
              }
            }
            OFL=FL/length(pok[,7])
            OFOA=FOA/length(pok[,7])
            OFH=FH/length(pok[,7])
            ONO=NO/length(pok[,7])
            OP=P/length(pok[,7])
            ORF=RF/length(pok[,7])
            OST=ST/length(pok[,7])
            OSTF=STF/length(pok[,7])
            OTOA=TOA/length(pok[,7])
            OTP=TP/length(pok[,7])
            pokerH=c("ROYAL FLUSH","STRAIGHT FLUSH","FOUR OF A KIND","FULL HOUSE","FLUSH","STRAIGHT","THREE OF A KIND", "TWO PAIR"
                     ,"PAIR","HIGH CARD")
            pokerO=c(ORF,OSTF,OFOA,OFH,OFL,OST,OTOA,OTP,OP,ONO)
            pokerT=c(RF,STF,FOA,FH,FL,ST,TOA,TP,P,NO)""")

st.write("jadi didapatkan kemungkinan sebagai berikut")
df3=pd.read_csv("dataodd.csv")
df3
st.markdown("""Berikut simulasi montecarlo dengan 500 perulangan dan visualisasinya \n
            set.seed(555)
            test2=sample(pokerH,500,replace = T,prob = pokerO)
            df2=data.frame(test2)
            ggplot(df2,aes(x=test2))+
              geom_bar()""")
st.image("montgra.png")
st.write(""" Jadi bisa dilihat bahwa hasil grafik simulasi memiliki bentuk yang hampir sama dengan bar cahrt data sebenarnya
         , tetapi bisa dilihat pada simulasi tidak terdapat royal flush, hal ini bisa dijelaskan dengan kemungkinan mendapatkan
         royal flush sangat kecil, jadi terdapat kemungkinan royal flush tidak terjadi simulasi.
""")

st.markdown("""monte carlo juga dapat digunakan untuk mencari perkiraan probabilitas terjadinya suatu kejadian  
            contohnya: dalam 10 tangan, berapa probabilitas mendapatkan 2 atau lebih flush?  
            berikut kodenya di R \n
            set.seed(555)
            runs <- 100000
            play=function(){
              u=0
              result=sample(pokerH,10,replace = T,prob = pokerO)
              for (x in 1:length(result)) {
                if(result[x]=="FLUSH"){
                 u=u+1
                }
              }
              return(u>=2)}
            flprob=sum(replicate(runs,play()))/runs
            flprob""")
st.write("jadi didapatkan probabilitas sekitar 0.03092 atau 3.092%")


st.subheader("Markov Chain")
st.markdown(""" untuk markov chain kita perlu menjadikan data kategorik dulu terus membuatmatix sequence \n
            mysequence<-df5$daily.returns
           df5$trend = cut(df5$daily.returns, c(-1, 0, 1))
           mysequence<-df5$trend
""")

st.markdown(""" membuat markov chain \n
            myFit<-markovchainFit(data=mysequence,confidencelevel = .9,method = "mle")
            myFit
""")
st.image("markov1.png")

st.markdown("""terus saya akan membuat ulang markov chain dengan label yang lebih mudah dimengerti \n
            mF<-myFit$estimate
            a11=mF[1,1]
            a12=mF[1,2]
            a21=mF[2,1]
            a22=mF[2,2]
            stateNames <- c("Down","Up")
            DU <- matrix(c(a11,a12,a21,a22),nrow=2, byrow=TRUE)
            dtmcA <- new("markovchain",transitionMatrix=DU, states=c("Down","Up"), name="MarkovChain A") 
            dtmcA
            """)
st.image("markov2.png")

st.markdown(""" mevisualisasikan markov chain \n
            plot(dtmcA)""")
st.image("marplot.png")
st.write("jadi jika dalam down saham memiliki probabilitas sekitar 51% untuk tetap down dan sekitar 49% untuk menjadi up dan jika dalam state up memiliki probabilitas sekitar 60% untuk menjadi down dan sekitar 40% untuk tetap up")
st.markdown("""untuk mengecek kemungkinan state akhir data dapat dilakukan dengan steady states \n
            steadyStates(dtmcA)
""")
st.image("ssmar.png")
st.write("jadi di akhir stock bca memiliki kemungkinan untuk turun dari nilai awal sekitar 55% dan kemungkinan naik dari nilai awal sekitar 44.9%")


st.subheader("Hidden Markov Model (HMM)")
st.markdown("""membuat hidden markov model \n
            hmm_model <- depmix(daily.returns ~ 1, family = gaussian(), nstates = n_states, 
                    data = df5)
            set.seed(555)
            hmm_fit <- fit(hmm_model)
            summary(hmm_fit)
""")
st.image("hmm.png")
st.write("""Jadi dari hasil hmm didapatkan 2 state, 2 state tersebut adalah tren market turun dan tren market naik,
         jadi pada saat tren market turun terdapat probabilitas sekitar 98.3% untukn tren tetap turun dan 1.7% untuk menjadi tren naik,
         dan pada saat tren naik terdapat probabilitas sekitar 95.2% untuk tren tetap naik dan sekitar 4.8% untuk menjadi tren turun.
""")
st.subheader("Evalutation and Discussion")
st.write(""" simulasi monte carlo berguna untuk menemukan nilai dan probabilitas sesuatu kejadian terjadi,  
         markov model berguna untuk menemukan kemungkinan untuk perubahan state suatu kejadian   
         dan  hidden markov model berguna untuk menemukan state tersebunyi dan probabilitas state tersebunyi tersebut berganti.
""")
st.write(""" Monte carlo memiliki kelebihan dimana mudah dilakukan, dapat mendapatkan hasil yang cukup akurat, dan memiliki kecepatan yang cepat,
         akan tetapi memiliki keterbatasan dimana, jika hanya dilakukan sedikit simulasi hasil akan menjadi kuarang atau tidak akurat, dan jarang memberi hasil yang exact.  
        markov chain dapat mendapat kemungkinanya sesuatu terjadi dan dapat memprediksikan kemungkinanya seusuatu terjadi dimasa depan,
         karena markov chain hanya melihat keaadan saat ini, maka markov chain tidak dapat menghitung probabilitas untuk sesuatu kejadian jika status kedaannya dimasa lalu juga mempengaruhi status dimasa depanya.  
         hidden markkov model membolehkan kita menggammbarkan sistem yang hidden dan menghitung probabilitasnya untuk berganti,
         hidden markov model memiliki kekurangan dimana ia membutuhkan data yang besar dan juga memiliki kesusahaan jika menghitung jumlah state yang banyak atau jika state memiliki interaksi yang kompleks.
""")
st.write("""jadi monte carlo, markov chain dan hidden markov model memiliki kegunaan yang berbeda,   
         monte carlo digunakan untuk mendapatkan suatu nilai atau probabilitas dari suatu kejadian,  
         markov chain digunakan untuk meilihat probabilitas berubahnya suatu state kejadian ,  
         dan hidden markov model digunakan untuk melihat dan menghitung probabilitas perubahan state dari suatu kejadian susah diamati sendiri.
""")
