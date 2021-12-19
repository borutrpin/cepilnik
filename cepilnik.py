#!/usr/bin/env python3
# -**- coding: utf-8 -**-
"""
Created on Fri Dec 17 16:48:04 2021
"""    

import streamlit as st
import datetime

st.set_page_config(
page_title="Cepilni kalkulator",
page_icon="💉",
layout="wide"
)
st.write(""" S tem orodjem lahko ugotovite, kakšna so vaša cepilna priporočila.""")
st.write("Pripravljeno po priporočilih NIJZ (november 2021)")
st.write("Izračuni so informativne narave.")
cepivo = st.selectbox(
     'Ali ste cepljeni?',
     ('ne', 'mRNA cepivo (Pfizer ali Moderna)','vektorsko cepivo Astra Zeneca','vektorsko cepivo Janssen',"mešana shema (Pfizer+Moderna, AZ+Pfizer itd)"))
preboleli = st.selectbox(
    'Ali ste preboleli covid?',
    ('ne','ja'))
if cepivo == "ne" and preboleli == "ne":
    st.write("Čimprej se cepite!")
else:
    if preboleli == "ne":
        if cepivo!="vektorsko cepivo Janssen":
            polnocepljeni = st.selectbox("Ali ste že polno cepljeni (2 dozi)?",
                       ("ja","ne"))
        else:
            polnocepljeni="ja"
        if polnocepljeni == "ja":
            kdajpolnocepljeni = st.date_input("Kdaj ste bili polno cepljeni (dve dozi oz. 1 v primeru Janssen)? (LETO/MM/DD)",datetime.date(2021,11,30))
            if cepivo=="vektorsko cepivo Janssen" or cepivo=="vektorsko cepivo Astra Zeneca":
                st.write("Pojdite po poživitveni odmerek z mRNA cepivom (Pfizer ali Moderna) od: "+str(kdajpolnocepljeni+datetime.timedelta(days=60))+"(LETO-MESEC-DAN) dalje.**")
                st.write("** od 18 do 30 let: Pfizer")
                st.write("** nad 30 let: Pfizer ali Moderna (1/2 odmerka)")
            elif cepivo=="mRNA cepivo (Pfizer ali Moderna)" or cepivo=="mešana shema (Pfizer+Moderna, AZ+Pfizer itd)":
                st.write("Pojdite po poživitveni odmerek z mRNA cepivom (Pfizer ali Moderna) od: "+str(kdajpolnocepljeni+datetime.timedelta(days=180))+" (LETO-MESEC-DAN) dalje.**")
                st.write("** od 18 do 30 let: Pfizer")
                st.write("** nad 30 let: Pfizer ali Moderna (1/2 odmerka)")
        else:
            st.write("Pojdite po drugi odmerek na predviden datum.")
            if cepivo=="vektorsko cepivo Astra Zeneca":
                st.write("Vsaj dva meseca po drugem odmerku pojdite po poživitveni odmerek z mRNA cepivom (Pfizer ali Moderna).")
                st.write("** od 18 do 30 let: Pfizer")
                st.write("** nad 30 let: Pfizer ali Moderna (1/2 odmerka)")
            elif cepivo=="mRNA cepivo (Pfizer ali Moderna)" or cepivo=="mešana shema (Pfizer+Moderna, AZ+Pfizer itd)":
                st.write("Vsaj šest mesecev po drugem odmerku pojdite po poživitveni odmerek z mRNA cepivom (Pfizer ali Moderna).")
                st.write("** od 18 do 30 let: Pfizer")
                st.write("** nad 30 let: Pfizer ali Moderna (1/2 odmerka)")
                st.write("Najbrž: Poživitveni odmerek kasneje NE BO potreben, a bo možen na lastno željo.")

    if preboleli == "ja":
        kdajpreboleli = st.date_input("Kdaj se je začela bolezen covid-19? (LETO/MM/DD)",datetime.date(2021,3,15))
        if cepivo=="ne":
            st.write("Opcija 1: Cepite se z enim odmerkom cepiva najkasneje do: "+str(kdajpreboleli+datetime.timedelta(days=270))+" (LETO-MESEC-DAN).**")
            st.write("Opcija 2: Cepite se z dvema odmerkoma cepiva od: "+str(kdajpreboleli+datetime.timedelta(days=270))+" (LETO-MESEC-DAN) dalje.**")
            st.write("** od 18 do 30 let: Pfizer")
            st.write("** nad 30 let: Pfizer ali Moderna (1/2 odmerka)")
            st.write("****:PCT pogoje izpolnjujete do: "+str(kdajpreboleli+datetime.timedelta(days=180)))
        elif cepivo=="vektorsko cepivo Janssen":
            kakopreboleli = st.selectbox("Kdaj ste preboleli covid?",
                                      ("pred cepljenjem","po cepljenju"))
            if kakopreboleli == "pred cepljenjem":
                st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
            else:
                st.write("Poživitveni odmerek NI potreben.")     
        elif cepivo=="mešana shema (Pfizer+Moderna, AZ+Pfizer itd)":
            kakopreboleli = st.selectbox("Kdaj ste preboleli covid?",
                                      ("pred prvo dozo","po prvi dozi","po drugi dozi"))

            if kakopreboleli == "pred prvo dozo":
                kdajodmerek1 = st.date_input("Kdaj ste prejeli prvi odmerek cepiva? (LETO/MM/DD)",datetime.date(2021,3,15))
                if kdajodmerek1-kdajpreboleli>datetime.timedelta(days=270):
                    drugiodmerek=st.selectbox("Ali ste že prejeli drugi odmerek cepiva?",("ne","ja"))
                    if drugiodmerek=="ne":
                       st.write( "Pojdite po drugi odmerek na predviden datum.")
                       st.write("Najbrž: Poživitveni odmerek kasneje NI potreben, a je možen na lastno željo.")   
                    else:
                        st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                else:
                    st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
            elif kakopreboleli== "po prvi dozi":
                odmerek2=st.selectbox("Ali ste že prejeli drugi odmerek cepiva?",("ne","ja"))
                if odmerek2=="ja":
                    kdajodmerek2 = st.date_input("Kdaj ste prejeli drugi odmerek?")
                    if kdajodmerek2-kdajpreboleli>datetime.timedelta(days=270):
                       st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                    else:
                        st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                else:
                       st.write( "Pojdite po drugi odmerek cepiva.")
                       st.write("Najbrž: Če dobite drugi odmerek do: "+str(kdajpreboleli+datetime.timedelta(days=270))+" (LETO-MESEC-DAN), potem poživitveni odmerek NE BO potreben, a bo možen na lastno željo.")
                       st.write("Najbrž: Tudi če dobite drugi odmerek kasneje od: "+str(kdajpreboleli+datetime.timedelta(days=270))+" (LETO-MESEC-DAN), potem poživitveni odmerek NE BO potreben, a bo možen na lastno željo.")
            else:
                st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                
        else:
            kakopreboleli = st.selectbox("Kdaj ste preboleli covid?",
                                      ("pred prvo dozo","po prvi dozi","po drugi dozi"))

            if kakopreboleli == "pred prvo dozo":
                kdajodmerek1 = st.date_input("Kdaj ste prejeli prvi odmerek cepiva? (LETO/MM/DD)",datetime.date(2021,3,15))
                if kdajodmerek1-kdajpreboleli>datetime.timedelta(days=270):
                    drugiodmerek=st.selectbox("Ali ste že prejeli drugi odmerek cepiva?",("ne","ja"))
                    if drugiodmerek=="ne":
                       st.write( "Pojdite po drugi odmerek na predviden datum.")
                       st.write("Poživitveni odmerek kasneje NI potreben, a je možen na lastno željo.")   
                    else:
                        st.write("Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                else:
                    st.write("Poživitveni odmerek NI potreben, a je možen na lastno željo.")
            elif kakopreboleli== "po prvi dozi":
                odmerek2=st.selectbox("Ali ste že prejeli drugi odmerek cepiva?",("ne","ja"))
                if odmerek2=="ja":
                    kdajodmerek2 = st.date_input("Kdaj ste prejeli drugi odmerek?")
                    if kdajodmerek2-kdajpreboleli>datetime.timedelta(days=270):
                       st.write("Najbrž: Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                    else:
                        st.write("Poživitveni odmerek NI potreben, a je možen na lastno željo.")
                else:
                       st.write( "Pojdite po drugi odmerek cepiva.")
                       st.write("Če dobite drugi odmerek do: "+str(kdajpreboleli+datetime.timedelta(days=270))+" (LETO-MESEC-DAN), potem poživitveni odmerek NE BO potreben, a bo možen na lastno željo.")
                       st.write("Najbrž: Tudi če dobite drugi odmerek kasneje od: "+str(kdajpreboleli+datetime.timedelta(days=270))+" (LETO-MESEC-DAN), potem poživitveni odmerek NE BO potreben, a bo možen na lastno željo.")
            else:
                st.write("Poživitveni odmerek NI potreben, a je možen na lastno željo.")