### user_activity_pipeline

#### Projektin yleiskuvaus
User Activity Pipeline on data engineering -projekti, jonka tarkoituksena on simuloida, prosessoida ja visualisoida käyttäjäaktiviteettidataa. Projekti generoi synteettistä käyttäjädataa, prosessoi sen reaaliajassa Apache Kafkan avulla ja tallentaa sen MongoDB-tietokantaan jatkoanalyysiä ja visualisointia varten. Projektille luotiin Streamlitillä interaktiivinen dashboard, joka tarjoaa näkymiä aktiviteettidataan.

#### Käytetyt työkalut ja kirjastot
1. Apache Kafka: Reaaliaikaisen datavirran käsittelyyn.
2. MongoDB: Käyttäjäaktiviteettidatan tallennustietokantana.
3. Streamlit: Interaktiivisen dashboardin luomiseen datan visualisointia varten.
4. Python-kirjastot:
   - confluent-kafka: Kafkan integroimiseen Pythonin kanssa.
   - pymongo: MongoDB:n käsittelyyn.
   - pandas: Datan muokkaamiseen ja analysointiin.
   - matplotlib: Visualisointien luomiseen.

#### Projektin työnkulku
1. Datan generointi:
   - Python-skripti data_generator.py generoi synteettistä käyttäjäaktiviteettidataa. Aktiviteetit sisältävät toimintoja, kuten kirjautuminen, uloskirjautuminen, osto, tuotteen katselu ja ostoskoriin lisääminen.
   - Data lähetetään Kafka-topiciin nimeltä user_activity.

2. Datan käsittely:
   - Python-skripti data_consumer.py kuluttaa datan Kafka-topicista ja tallentaa sen MongoDB-kokoelmaan nimeltä user_activity.

3. Datan visualisointi:
   - Dashboard-skripti dashboard.py hakee datan MongoDB:stä ja luo visualisointeja sen analysoimiseksi.

#### Projektin skriptit
1. data_generator.py:
   - Generoi synteettistä käyttäjäaktiviteettidataa.
   - Lokittaa aktiviteetit ja lähettää datan Kafkaan.

2. data_consumer.py:
   - Lukee datan Kafka-topicista.
   - Tallentaa datan MongoDB:hen.

3. dashboard.py:
   - Luo visualisointeja Streamlitin avulla.
   - Yhdistää MongoDB:hen datan hakemista ja näyttämistä varten.

#### Visualisoinnit
1. Aktiviteettijakauma:
   - Näyttää, kuinka monta kertaa kutakin aktiviteettityyppiä (esim. osto, kirjautuminen, tuotteen katselu) on tehty.

2. Käyttäjäkohtainen aktiviteettimäärä:
   - Korostaa 10 aktiivisinta käyttäjää.

3. Ostojen kehitys ajan myötä:
   - Näyttää ostojen määrän kehityksen ajan funktiona.

#### Ohjeet projektin toistamiseen
1. Kafka- ja MongoDB-palveluiden asennus ja käynnistys:
   - Käynnistä Zookeeper- ja Kafka-palvelimet.
   - Varmista, että MongoDB toimii paikallisesti.

2. Suorita skriptit:
   - Aja data_generator.py tuottaaksesi ja lähettääksesi dataa Kafkaan.
   - Aja data_consumer.py prosessoidaksesi datan ja tallentaaksesi sen MongoDB:hen.
   - Aja dashboard.py seuraavalla komennolla nähdäksesi dashboardin:
     streamlit run dashboard.py

#### Lisenssi
Tämä projekti on lisensoitu MIT-lisenssillä.
