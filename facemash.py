import streamlit as st
import random

if 'contador' not in st.session_state:
    st.session_state.contador = 0

imagens = ['andre.jpg', 'dexter.webp', 'doakes.jpg', 'ben.webp', 'spider.jpg', 'hulk.png', 'ironman.png', 'patria.jpg', 'flash.jpg', 'batmangoat.webp','lulapreso.webp', 'wonder.jpg',  'superman.jpg', 'coringa.jpg', 'deadpool.jpg', 'onzesigma.jpg', 'messi.jpg', 'popocris.jpg', 'diddy.gif', 'pretog.jpg', 'gatocinza.png', 'mark.jpg', 'kirk.jpg', 'jarvis.jpeg', 'trump.jpg', 'salsicha.jpg', 'eita.jpg', 'tigrao.jpg', 'cavalo.jpg', 'sla.jpg', 'ronaldo.jpg', 'dino.jpg', 'mem.jpg']



c1 = random.choice(imagens)
c2 = random.choice(imagens)

st.title('Facemash')
st.write('quem vence? ')

col1, col2 = st.columns(2)

with col1: 
    st.image(f'{c1}')
    if st.button('Esquerda'):
        st.session_state.contador += 1
        st.rerun()

with col2:
    st.image(f'{c2}')
    if st.button('Direita'):
        st.session_state.contador += 1
        st.rerun()

st.write(f'Partidas jogadas: {st.session_state.contador}')

if st.session_state.contador == 20 and 100 and 500:
    st.write('Parabens você julgou +20 duelos!')
    st.balloons()

