import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/61/8f/08/618f083c61a7460ce0a6064319af41bd.gif");
            background-attachment: fixed;
            background-size: cover;
            /* opacity: 0.3; */
        }}
        [data-testid="stSidebar"]{{
           background-image: url(https://i.pinimg.com/564x/a2/61/f1/a261f178728a536eefc8f1e4e8f68c13.jpg);
           background-size: cover;
        }}
        </style>
        """,
    unsafe_allow_html=True
)
#---------------------------------------------------------------------------------background-------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["Home", "Type of game", "Model"])
with tab1:
   st.title('![image](https://i.pinimg.com/564x/0f/65/9b/0f659b65c7e5605dad53fba31a8ee8df.jpg)')

   code = '''
       ("Hello Gammer")'''
   st.code(code, language='python')
   code = '''
          print(" ..เชื่อกันว่าทุกคนคงจะเคยเล่นเกมกันใช่มั้ยครับ อย่างเช่นเกมยิงปืน เกมเเข่งรถ เกมมว่ายน้ำ 
หรือเกมเเนวพวกตีป้อม5v5เเละอื่นๆอีกมากมาย เเต่ผมเชื่อว่าบางคนอาจจะยังไม่รู้ว่าเเนวเกมเเต่ละเกมนั้น
มีชื่อเรียกของตัวมันเอง วันนี้ผมก็เลยจะพาทุกๆคนไปดูเกมเเต่ละประเภทกันอย่างคร่าวๆครับว่าจะมีอะไรกันบ้าง")'''
   st.code(code, language='python')


#----------------------------------------------------------------------------TAP1-------------------------------------------------------------------------------------------

with tab2:
   left, right = st.columns(2)
   Right = right.markdown('![imgae](https://i.pinimg.com/originals/21/24/82/2124829c7a43bc576bdb3129cbcaed89.gif)')
   Lelf = left.markdown('![image](https://i.pinimg.com/originals/4a/f9/7b/4af97be15a1edae3f1b61cdb0a60d30a.gif)')
   st.title("TYPES of GAMES" ':video_game:'  '')
   original_list = ['Type of game ', 'Actionrog', 'FPS', 'Racing', 'Sportgame', 'DungeonCrawling']
   All_game = st.selectbox('Type your name game ', original_list)
   selected_option = ('Choose an option:', All_game)

#------------------------------------------------------------------------------------------TAP2------------------------------------------------------------------------------------

with tab3:
    pow = st.selectbox('Choose Game', ['Pickone Type','Actionrog', 'FPS','Racing','Sportgame','DungeonCrawling'])
    if pow == 'Actionrog':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book11.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('Picture/Book11.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('Picture/Book11.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")

#______________________________________________________________________________________________Actionrog---------------------------------------------------------------------
    if pow == 'FPS':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book12.1.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('Picture/Book12.1.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('Picture/Book12.1.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")

#----------------------------------------------------------------------------------------------FPS---------------------------------------------------------------------------------
    if pow == 'Racing':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book13.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('Picture/Book13.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('Picture/Book13.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")

#---------------------------------------------------------------------------------------------------Racing-------------------------------------------------------------------------

    if pow == 'Sportgame':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book14.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('Picture/Book14.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('Picture/Book14.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")


#------------------------------------------------------------------------------------------------------------------------Sportgame-------------------------------------------------------

    if pow == 'DungeonCrawling':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('Picture/Book15.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('Picture/Book15.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('Picture/Book15.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")



#-------------------------------------------------------------------------------------------Tab---------------------------------------------------------------------------------

st.sidebar.markdown('![image](https://i.pinimg.com/originals/40/cb/70/40cb707f4cf722302891471e0c86409c.gif)')


#--------------------------------------------------------------------------------Lits-Addlit------------------------------------------------------------------------------------


#def Save_Actionrog(Action_rog):
  #   return Action_rog (Action_rog,'Action_rog','FPS','Racing')


if All_game == 'Actionrog':
    st.write('Hello gamemer')
    st.markdown('## ROG')
    st.title('1.New World')
    st.markdown('![image](https://img.my-best.in.th/product_images/ec7cdf00bf9ff31757e465b25f1e3e94.jpg?ixlib=rails-4.2.'
                '0&q=70&lossless=0&w=640&h=640&fit=clip&s=790c75fcd641949a81044fdd245741d8)')

    st.write('เกมที่มีการนำเสนอความคลาสสิกออกมาได้อย่างน่าประทับใจมาก')
    st.write('อีกกหนึ่งเกม MMORPG ที่เปิดให้บริการมาอย่างยาวนาน หลาย ๆ คนอาจจะคิดว่าเกม MMORPG '
             'ยุคใหม่จะเน้นกราฟิกที่สวยงาม ฉากและเรื่องราวที่น่าตื่นเต้น แต่ Toram Online ไม่ได้เป็นแบบนั้น '
             'เพราะเกมนี้มีการนำเสนอความคลาสสิกออกมาได้อย่างน่าสนใจ มีการนำเสนอเกมด้วยภาพที่ไม่ใช่ภาพสมัยใหม่ แต่สวยงาม ระบบต่าง ๆ '
             'ผู้เล่นจะต้องดำเนินการเอง ไม่มีระบบช่วยสอนหรือระบบอัตโนมัติช่วยเหมือนเกมอื่น ๆ ใครที่ชอบเกมเก็บเลเวลที่มีบรรยากาศคลาสสิก เกมนี้เป็นตัวเลือกที่ดีครับ')
    st.write('Download >> https://www.newworld.com/en-us')

    st.write('2.Endwalker')
    st.markdown('![image](https://img.my-best.in.th/product_images/d45cb1e67e76f98298c7bd26150334a7.jpg?ixlib=rails-4.2.'
                '0&q=70&lossless=0&w=640&h=640&fit=clip&s=34dba6b5a620b6d66b1aaae3a3395283)')
    st.write(
        '   เกมที่ Square Enix ทีมผู้พัฒนายักษ์ใหญ่จากญี่ปุ่นเปิดตัวมาเพื่อเป็นภาคเสริมของภาค XIV กับเรื่องราวบทสรุปการผจญภัย '
        'คลาสอาชีพใหม่ และแผนที่เพิ่มเติม ให้ผู้เล่นสำรวจมากกว่าเดิม โดยในส่วนเนื้อหาเป็นการเล่าเรื่องของเหล่า Ascian ที่พยายามทำลายล้างทุกอย่าง'
        ' ซึ่งคลาสใหม่ภายในเกมคือ Sage อาชีพสาย Healer และ Reaper อาชีพสายโจมตีระยะประชิด นอกจากนี้ ยังมีการเพิ่มชนเผ่าใหม่อย่าง Arkasodara เข้ามา'
        ' และมีการเพิ่มดันเจี้ยนให้มากขึ้นอีกด้วย อย่างไรก็ตาม ผู้เล่นต้องทำการเล่นเนื้อหาในภาคก่อนอย่าง Heavensward หรือ Stormbloog มาแล้ว จึงจะสามารถเล่นภาคนี้ได้ครับ')
    st.write('Download >> https://www.newworld.com/en-us')


    st.write('3.Toram Online')
    st.markdown('![image](https://img.my-best.in.th/product_images/33b5e71b6a27eb66ade4fc5e4e8cbc09.jpg?ixlib=rails-4.2.'
                '0&q=70&lossless=0&w=640&h=640&fit=clip&s=3686a141c32155b5b48f716dc7d8b098)')
    st.write('เกมที่มีการนำเสนอความคลาสสิกออกมาได้อย่างน่าประทับใจมาก')
    st.write('  อีกหนึ่งเกม MMORPG ที่เปิดให้บริการมาอย่างยาวนาน หลาย ๆ คนอาจจะคิดว่าเกม MMORPG ยุคใหม่จะเน้นกราฟิกที่สวยงาม  '
             'ฉากและเรื่องราวที่น่าตื่นเต้น แต่ Toram Online ไม่ได้เป็นแบบนั้น เพราะเกมนี้มีการนำเสนอความคลาสสิกออกมาได้อย่างน่าสนใจ '
             'มีการนำเสนอเกมด้วยภาพที่ไม่ใช่ภาพสมัยใหม่ แต่สวยงาม ระบบต่าง ๆ ผู้เล่นจะต้องดำเนินการเอง ไม่มีระบบช่วยสอนหรือระบบอัตโนมัติช่วยเหมือนเกมอื่น ๆ '
             'ใครที่ชอบเกมเก็บเลเวลที่มีบรรยากาศคลาสสิก เกมนี้เป็นตัวเลือกที่ดีครับ')
    st.write('Download >>  https://en.toram.jp/')

    st.write('4.The Witcher 3 Wild Hunt')
    st.markdown('![image](https://i.pinimg.com/564x/7a/7e/e8/7a7ee89918563d4bfc939a3ceeb9744d.jpg)')
    st.write('ผลงานระดับขึ้นหิ้งจากค่ายนักพัฒนาเกมชาวโปแลนด์ CD Projekt Red ที่ได้สร้างชื่อเสียงไปทั่ววงการเกม The Witcher 3 Wild Hunt ผู้เล่นจะได้รับบทเป็น Geralt of Rivia '
             'ซึ่งเราจะต้องตามหา Ciri ลูกสาวบุญธรรมที่หายตัวไป โดยตัวเกมจะมีกิจกรรมต่างๆ ให้เราทำมากมายพร้อมทั้งเนื้อเรื่องสุดเข้มข้นที่เล่นแล้วแทบจะวางจอยไม่ลงกันเลยทีเดียว')
    st.write('Download >> https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/')

    st.write('5.Final Fantasy XV')
    st.markdown('![image](https://i.pinimg.com/564x/33/71/6c/33716ce6051a3f24a75b40b055a68301.jpg)')
    st.write('อีกหนึ่งซีรี่ส์เกม RPG ในตำนานที่ที่ไม่ว่าจะออกมากี่ภาคก็ยังคงครองใจเหล่าเกมเมอร์มาจนถึงปัจจุบันอย่าง Final Fantasy XV โดยในภาคนี้จะเป็นเรื่องราวเกี่ยวกับเจ้าชาย Noctis กับเหล่าสหายทั้ง 3 คน'
             ' ที่จะต้องกลับมาทวงบัลลังก์หลังจากที่อาณาจักรของพวกเขาถูกยึดครองโดย Niflheim '
             'ซึ่งตัวเกมภาคนี้ก็ได้เพิ่มระบบความเป็นเกม Action มากขึ้นทำให้การต่อสู้มีความสะใจมากยิ่งขึ้นด้วยและในส่วนของเนื้อเรื่องที่น่าติดตามเช่นเดียวกัน ใครเป็นแฟนซีรี่ส์นี้ไม่ควรพลาดด้วยประการทั้งปวงครับ')
    st.write('Download >> https://store.steampowered.com/agecheck/app/637650/')

if All_game == 'FPS':
    st.markdown('## FPS First Person Shooting')
    st.write('1.PlayerUnknown Battlegrounds ')
    st.image('Picture/pubg.JFIF')
    st.write('  PUBG นั้นเป็นเกมแนวใหม่ที่เพิ่งเกิดขึ้นได้ไม่นานทำให้มีวิธการเล่นที่ค่อนข้างกับแบบเดิม ๆ ที่เรารู้จักกันมาก่อน โดยการเล่นนั้นจะเป็นแบบทีม 4 คนหรือจะมาเป็นคู่ หรือเดี่ยวก็ได้'
             'โดยในหนึ่งแมทช์นั้นจะประกอบไปด้วยผู้เล่นทั้งหมด 100 คนและจะลงไปบนแผนที่ด้วยตัวเปล่าก่อนที่เราจะต้องออกไปหาอุปกรณ์ต่าง ๆ มาใส่เสริมให้ตัวเราเอง นอกจากนี้จะมีตัวกำหนดเลยก็คือ’วง’ '
             'ที่จะบีบเข้ามาเรื่อย ๆ เพื่อบังคับให้ผู้เล่นต้องสู้กันเพื่อหาว่าใครหรือกลุ่มไหนจะได้เป็นผู้เหลือรอดสุดท้ายนั่นเอง')
    st.write('Download >> https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/?l=thai')

    st.write('2.Apex Legends')
    st.image('Picture/ape.JPG')
    st.write('  เกม Apex Legends นั้นถูกทดสอบมาหลากหลายรูปแบบเป็นอย่างมากจนในที่สุดพวกเขาก็ได้ข้อพิสูจน์แล้วว่าการเล่นแบบ 3 คนต่อหนึ่งทีมเป็นการเล่นที่ดีที่สุด '
             'โดยจะมีตัวให้เลือกทั้งหมด 8 ตัว (มีอีก 3ตัวเพิ่มเข้ามา) ในตอนนี้ ซึ่งคาดเดากันว่าจะมีเพิ่มเติมมากขึ้นอีกในอนาคตข้างหน้า สำหรับแต่และตัวละคร (Legends) นั้นจะมีสกิลทั้งหมด 3 '
             'สกิลด้วยกันซึ่งจะต่างกันไปในแต่ละตัว โดยสามารถดูได้ที่บทความ ทักษะตัวละครทั้ง 8 ในหนึ่งการแข่งขันจะมีทีมทั้งหมด 20 ทีมนับเป็นจำนวนผู้เล่น 60 คนต่อการเล่นหนึ่งครั้งซึ่งมีข่าวว่าในอนาคตข้างหน้านอกจากโหมดแบบ 3 คนต่อ 1 '
             'ทีมแล้วนั้นจะมีโหมดแบบตะลุยเดี่ยวหรือแบบคู่หูออกมาให้กับผู้เล่นได้เล่นกัน')
    st.write('Download >> https://store.steampowered.com/app/1172470/Apex_Legends/?l=thai')

    st.write('3.Warface')
    st.image('Picture/warface.JFIF')
    st.write('อีกหนึ่งเกม FPS สู้รบทางทหารจาก Crytek ที่พัฒนาและอัปเดตมาอย่างยาวนานเกือบสองทศวรรษ ที่เปิดตัวบน PC ก่อน ก่อนจะเปิดให้บริการบน Xbox One และ PS4 ในปลายปีนี้ '
             'โดยเกมจะเน้นไปที่การเล่นร่วมกันหลายคน (Multiplayer) ที่ต้องคอยช่วยเหลือกันแบ่งไปตามความถนัดของตัวละคร')
    st.write('Download >> https://store.steampowered.com/agecheck/app/291480/')

    st.write('4.Call of Duty')
    st.markdown('![image](https://i.pinimg.com/564x/24/46/41/244641628b42e9e014c6533eb1f2e5d9.jpg)')
    st.write('เกม FPS อันทรงเสน่ห์แบบมีเอกลักษณ์เฉพาะตัว อัดแน่นไปด้วยเนื้อหาสุดเข้มข้นที่ผู้เล่นต้องรับบทเป็น CIA ทหารนาวิกโยธินและทำภารกิจต่าง ๆ ตามคำสั่งทั่วโลก'
             ' แม้บางเรื่องอาจไม่ถูกต้องตามศีลธรรมแต่ถ้าเทียบในชีวิตจริงคุณต้องตัดสินใจว่าควรทำอย่างไร กลายเป็นจุดเด่นสุดพิเศษที่ไม่ควรพลาดเด็ดขาด')
    st.write('Download >> https://www.callofduty.com/modernwarfare/pc')

    st.write('5.Atomic Heart')
    st.markdown('![image](https://i.pinimg.com/564x/59/45/3c/59453cdd28fefb24fd8ba0808fd525aa.jpg)')
    st.write('เกมนี้ถือเป็นน้องใหม่แห่งวงการ FPS แต่จัดเต็มความมันส์ระเบิดแน่นอน เมื่อในโลกของเกมสหภาพโซเวียตเกิดความเจริญรุ่งเรือง ลัทธิคอมมิวนิสต์เฟื่องฟูมาจนถึงปัจจุบัน'
             ' ผู้เล่นต้องสวมบทบาทเป็นสายลับเพื่อเข้ามาสืบสวนการทดลองบางอย่างพร้อมเอาตัวรอดจากกองทัพหุ่นยนต์ไม่สมประกอบ '
             'จุดเด่นคือภาพที่แอบสยองขวัญ มีความหลอนในตัว เล่นแล้วให้อารมณ์สมจริงสุด ๆ')
    st.write('Download >> https://atomic-heart.en.softonic.com/')

if All_game == 'Racing':
    st.markdown('## RACING')
    st.markdown('![image](https://i.pinimg.com/originals/87/81/2d/87812d6c1c30d7678d6b084d08ded25d.gif)')
    st.write('1.Dirt Rally 2.0')
    st.markdown('![image](https://i.pinimg.com/564x/42/b3/24/42b3242d1f4c9c7a0d8e2ce4c177a947.jpg)')
    st.write('Dirt Rally 2.0 โดย Codemasters คือการจำลองการแข่งแรลลี่อย่างแท้จริง ภายในโลกนี้เป็นการจำลองความรู้สึกของการแข่งรถแรลลี่ '
             'เพื่อให้นักซิ่งได้สัมผัสเกมแข่งรถเหมือนจริงและไม่รั้งผู้เล่นไว้ในการฝึกสอนเล่นและการอธิบายคอนเซปต์เกมมากมาย '
             'ดังนั้นผู้เล่นใหม่ที่ไม่เชี่ยวชาญกับวงการรถยนต์มากนักอาจรู้สึกว่ายากในช่วงแรกๆ แต่มันก็มอบเกมเพลย์ รายละเอียด และความสมจริงที่ลึกล้ำที่เหล่าแฟนๆ ต่างชื่นชอบ')
    st.write('Dowload >> https://store.steampowered.com/app/690790/DiRT_Rally_20/?l=thai')

    st.write('2.Grid 2')
    st.markdown('![image](https://i.pinimg.com/564x/c4/0e/25/c40e255645a35fd8b66edb2ed39d37c7.jpg)')
    st.write('Grid 2 เป็นเกมอีกเกมจากค่าย Codemasters เกมที่แปดจากซีรีส์ TOCA Touring Car เกมนี้มีเป้าหมายในการเกมที่เข้าถึงได้ง่ายมากขึ้น'
             ' ผสมผสานการจำลองการขับรถอย่างเข้มข้นและรูปแบบการควบคุมเกมแบบอาร์เคดที่ควบคุมได้ง่ายได้อย่างสมดุล เกมนี้ไม่เพียงมีรถมากมายหลายแบบให้เลือกแต่งได้ตามใจแต่ก็ยังให้ผู้เล่นได้มาอยู่ในลีกแข่งขันสมมติ '
             '"งานแข่งรถเวิลด์ซีรีส์" งานแข่งรถแบบใหม่ที่มีกฎที่ตั้งมาเพื่อเกมนี้โดยเฉพาะ โหมดแคมเปญ/โหมดเนื้อเรื่องอาชีพเสมือนจะให้คุณลองพยายามดึงดูด '
             '"แฟนๆ" ให้มาดูเกมรถแข่งใหม่นี้ด้วยการเล่นให้ผ่านเป้าหมายการแข่งขันต่างๆ ในแต่ละด่าน')
    st.write('Download >> https://steamunlocked.net/grid-2-free-download/')

    st.write('3.Assetto Corsa')
    st.markdown('![iamge](https://i.pinimg.com/564x/ab/25/1f/ab251f62d7bcc514bf7f1de4348bd464.jpg)')
    st.write('นักพัฒนาเกม Kunos Simulazioni พัฒนา Assetto Corsa ขึ้นเพื่อสร้างเกมสำหรับแฟนๆ '
             'ผู้คลั่งไคล้เกมรถแข่งโดยเป็นเกมที่เน้นไปที่การควบคุมรถและประสิทธิภาพของเกมอันแม่นยำพร้อมทั้งมอบการปรับแต่ง '
             '(หรือเพิ่มการปรับแต่งต่างๆ)'
             ' ประสบการณ์และการตั้งค่าด้วย ซีรีส์เกมที่ "สมจริง" ที่ให้แฟนๆ เกมรถแข่งสามารถปรับแต่งประสบการณ์ที่เขามองเห็นให้จำลองออกมา หรือไม่จำลองออกมาในเกมนั่นคือคุณสมบัติเด่นของ Assetto Corsa '
             'ซึ่งเป็นเกมเฉพาะทางสำหรับแฟนๆ ผู้คลั่งไคล้และติดตามเกมรถแข่งแบบเข้มข้น นักเล่นเกมสบายๆ ที่มองหาเกมสไตล์อาร์เคดที่มีความยากปานกลางอาจไม่เหมาะกับเกมนี้นักAssetto Corsa ไม่ใช่เกมรถแข่งที่เล่นได้ง่ายในทันที '
             'แต่เป็นเกมที่เหมาะกับผู้เล่นที่มีความรู้เกี่ยวกับรถระดับไฮเอนด์และมีทักษะในการขับขี่ด้วย'
             ' และสำหรับผู้เล่นเหล่านั้น Assetto Corsa ก็เป็นเหมือนขุมทรัพย์เลยทีเดียว')
    st.write('Dowload >> https://store.steampowered.com/app/244210/Assetto_Corsa/')

    st.write('4.Forza Horizon 4')
    st.markdown('![image](https://i.pinimg.com/564x/51/2d/01/512d01d36cae64a76b9eab3b78c1c7f6.jpg)')
    st.write('Forza Horizon 4 ได้โน้มเอียงเข้ามาเป็นส่วนหนึ่งของ "วิดีโอเกม" ที่ขับเคลื่อนบนเครื่องพีซี ทุกแง่มุมของเกมเพลย์ผ่านการ "ออกแบบเพื่อความสนุกสนาน" '
             'ไม่ว่าจะเป็นเสียงแสบสันของเอไอจีพีเอส ที่ชื่อว่า A.N.N.A. (แสบสันแบบ David Hasselhoff’s KITT จาก Knight Rider ผสมกับ Amazon’s Alexa) ที่จะช่วยบอกข้อมูลให้คุณรู้เกี่ยวกับเผ่าพันธุ์ต่างๆ '
             'และความท้าทายรอบตัวคุณเมื่อคุณออกสำรวจในโลกเปิด เธอยังช่วยทำสัญลักษณ์ที่ตำแหน่งความท้าทายโปรดบนแผนที่ของคุณให้คุณเข้าถึงได้ง่ายขึ้น')
    st.write('Download >> https://store.steampowered.com/app/1293830/Forza_Horizon_4/')

    st.write('5.The Crew 2')
    st.markdown('![image](https://i.pinimg.com/564x/c5/be/46/c5be462966ae701e62c85add673dad9d.jpg)')
    st.write('เกมนี้มีทั้งโหมด Street Racing, Off Road, Freestyle และ Pro Racing ซึ่งให้คุณเล่นเก็บความคืบหน้าได้อย่างสนุกสนานและสามารถเล่นได้แบบไม่เป็นเส้นตรง '
             'เล่นตามอารมณ์ตามที่คุณเห็นว่าความท้าทายไหนสนุกสำหรับคุณ The Crew 2 มอบการแข่งรถที่สนุกสนานและเป็นเกมรถแข่งที่เหมาะสำหรับผู้เล่นเกมรถแข่งทั่วๆ ไป เกมนี้จึงนับได้ว่าประสบความสำเร็จในบางประการ '
             'หากคุณมีเกมรถแข่งอยู่ในคลังอยู่แล้ว จะเก็บเกมนี้ไว้เพิ่มก็ไม่เลว แต่เกมนี้ก็อาจไม่สามารถไต่เต้าขึ้นมาเป็นเกมโปรดของคุณได้')
    st.write('Download >> https://store.steampowered.com/app/646910/The_Crew_2/')


if All_game == 'Sportgame':
    st.title('Sportgame')
    st.write('1.FIFA 22')
    st.markdown('![image](https://i.pinimg.com/564x/b2/e6/68/b2e668ee265c19beeb285999e9a5fb55.jpg)')
    st.write('ครองตำแหน่งเกมฟุตบอลที่สุด มีการพัฒนาที่หลากหลายกว่าเดิม')
    st.write('สำหรับ FIFA 22 ยังถือเป็นเกมกีฬาฟุตบอลที่ได้รับความนิยมมากที่สุด และในภาคได้นี้มีการปรับปรุงและพัฒนาในหลาย ๆ ด้าน ทั้งด้านของ A.I. ที่ทำให้บอทฉลาด'
             ' และมีไหวพริบมากขึ้น ผู้รักษาประตูเสียประตูยากกว่าเดิม อย่างไรก็ตาม จุดเด่นที่พลาดไม่ได้เลยก็คือ โหมด Career โดยในโหมด Manager Career'
             ' ผู้เล่นสามารถตั้งสโมสรของตนเองได้ สามารถปรับได้ตั้งแต่ตราสโมสร ชุดแข่ง จนถึงเพลงเชียร์ อีกทั้งในโหมด Player Career '
             'มีการเพิ่มระบบ Attributes ที่เราสามารถเลือกอัปเกรดค่าพลังตัวละครได้ และระบบ Perk ที่เป็นเหมือนสกิลพิเศษที่ช่วยในการแข่งขัน '
             'เช่น โยนบอลแม่นยำมากขึ้น หรือเลี้ยงบอลติดเท้ามากขึ้น ครับ')
    st.write('Dowload >> https://fo4.garena.in.th/download')

    st.write('2.CAPTAIN TSUBASA : RISE OF NEW CHAMPIONS')
    st.markdown('![image](https://i.pinimg.com/564x/7b/95/26/7b952682df4800e67b40f88e19f6cbc8.jpg )')
    st.write('ตำนานการ์ตูนสุดโด่งดัง สู่เกมที่เราได้สวมบทบาทตัวละครโปรด')
    st.write('จากการ์ตูนอันโด่งดัง วันนี้ได้กลายมาเป็นเกม CAPTAIN TSUBASA : RISE OF NEW CHAMPIONS ให้แฟน ๆ ได้จับจอง PS4 เล่นกัน '
             'โดยจุดเด่นที่สุดคือ ภาพที่เหมือนกับตัวการ์ตูนต้นฉบับไม่ผิดเพี้ยนเลยครับ ทั้งยังมาพร้อมตัวละครที่เราคุ้นตาอย่างโอโซระ ซึบาสะ หรือเฮียวงะอีกด้วย'
             ' ส่วนในโหมดเนื้อเรื่องก็มีให้เลือกด้วยกัน 2 รูปแบบที่พลาดไม่ได้คือ การสวมบทเป็นซึบาสะ โดยเล่นตามเรื่องราวที่ถอดออกมาจากการ์ตูน หรือจะเลือกเล่นแบบ '
             'New Hero ที่เราสามารถสร้างตัวขึ้นมาเองและเลือกเส้นทางอาชีพได้เองเลยครับว่า จะให้ตัวละครเดินทางเป็นนักฟุตบอลแบบใด')
    st.write('Download >> https://store.steampowered.com/app/1163550/Captain_Tsubasa_Rise_of_New_Champions/')

    st.write('3.1ssssssssssssw™ Pro Skater™ 1+2')
    st.markdown('![image](https://i.pinimg.com/564x/66/e6/4c/66e64ca44d8213fca77d7e4761014dc0.jpg)')
    st.write(' การกลับมาอีกครั้งของเกมสเก็ตบอร์ดในตำนาน สู่ภาพระดับ HD ')
    st.write('เกมเมอร์ที่อยู่ในวงการมานานน่าจะจำเกมในตำนานอย่าง Tony Hawk ที่ลงให้เล่นตั้งแต่เครื่อง PS2 ได้ใช่ไหมครับ วันนี้เขากลับมาอีกครั้งในเครื่อง PS4 ด้วยการยกระดับกราฟิกใหม่ทั้งหมด'
             ' มาพร้อมภาพระดับ HD ที่รองรับความคมชัดระดับ 4K เลยทีเดียว นอกจากนี้ ทีมงานยังได้เพิ่มท่าเล่นใหม่ ๆ เข้ามา และเพิ่มโหมดออนไลน์ไว้วัดคะแนนกับผู้เล่นทั่วโลก ส่วนใครที่เป็นสายแต่งตัวหรือแต่งสเก็ตบอร์ด '
             'เกมนี้ก็ได้จัดเต็มกับเสื้อผ้าที่มีให้เลือกแต่งตัวกันมากมาย พร้อมทั้งสามารถแชร์ให้คนอื่นได้ใช้ตัวละครของเรา รวมถึงสามารถสร้างสนามได้ในรูปแบบของตนเองเอาไว้ประลองท่าสุดล้ำแบบไม่เหมือนใครอีกด้วยครับ')
    st.write('Download >> https://store.epicgames.com/en-US/p/tony-hawks-pro-skater-1-and-2')

    st.write('4.AO Tennis 2')
    st.markdown('![image](https://i.pinimg.com/736x/34/48/ab/3448abb1a785ac2d4a64623601b91882.jpg)')
    st.write('เกมเทนนิสที่เน้นความสมจริง เหมาะสำหรับแฟนเทนนิสตัวยง')
    st.write('AO Tennis 2 ถูกยกระดับขึ้นมาจากภาคแรกในหลาย ๆ ด้าน โดยเฉพาะการเพิ่มโหมด Career ที่คุณจะได้สร้างนักเทนนิสขึ้นมาเอง '
             'พร้อมเลือกสไตล์การเล่นที่ชื่นชอบและเรียนรู้จากความพ่ายแพ้ ในโหมดนี้คุณยังต้องบริหารจัดการเรื่องนอกสนามด้วยครับ เช่น การหาสปอนเซอร์เข้ามาสนับสนุน '
             'การจัดการซ้อมหรือการจ้างโค้ช เพื่อให้เราก้าวขึ้นไปเป็นที่หนึ่งของโลก ซึ่งใน AO Tennis 2 จะเน้นความสมจริงเป็นอย่างมาก ดังนั้น '
             'ตัวละครที่เพิ่งสร้างของคุณจึงไม่สามารถเอาชนะนักเทนนิสมืออาชีพได้ง่าย ๆ อย่างแน่นอน หากคุณชอบความสมจริงและความท้าทาย เกมนี้ต้องมีติดเครื่อง PS4 เอาไว้เลยครับ')

    st.write('5.eFootball 2022')
    st.markdown('![image](https://i.pinimg.com/564x/18/bf/80/18bf80d6d8b60e8e9bd20f51a5a316e1.jpg)')
    st.write('การรีแบรนด์จากเกมฟุตบอลยอดฮิต PES สู่การแข่งขัน E-Sport')
    st.write('การเปลี่ยนแปลงครั้งใหญ่จากค่าย Konami ที่ทำการรีแบรนด์ PES ใหม่ในชื่อของ eFootball เพื่อยกระดับสู่เกมฟุตบอล E-Sport '
             'ที่ยิ่งใหญ่ที่สุดในโลก'
             ' โดยเปลี่ยนตัวเกมรูปแบบการให้บริการเป็นแบบ Free to Play ที่มาพร้อมระบบ'
             ' Cross Platform ที่สามารถแข่งขันได้ทุกอุปกรณ์ ไม่ว่าจะเป็น PS5, PS4, Xbox One, PC หรือแม้กระทั่งในสมาร์ทโฟน '
             'และถึงแม้ว่าการเปิดตัวจะมีกระแสที่ไม่ค่อยดีเท่าไหร่นัก ทั้งคำวิจารณ์ด้านการเคลื่อนไหว กราฟิก และการเปลี่ยนเกมเพลย์ อย่างไรก็ตาม ทาง '
             'Konami ได้ทำการอัปเดตเวอร์ชันใหม่เพื่อปรับสมดุล และแก้บัคต่าง ๆ ภายในเกมแล้วครับ')
    st.write("Download >> https://play.google.com/store/apps/details?id=jp.konami.pesam&gl=US&pli=1")


if All_game == 'DungeonCrawling':
    st.title('DungeonCrawling ')
    st.write('1.Diablo Series')
    st.markdown('![image](https://i.pinimg.com/564x/a7/e6/66/a7e66616754d47a0c0ea3c9f93281655.jpg)')
    st.write('Diablo ซีรี่ย์เกมในตำนานที่ถูกกล่าวขานไปอีกนานและยังเป็นรากฐานสำคัญการถือกำเนิดของเกมแนว dungeon crawlers อีกหลายเกมหนึ่งในนั้นคือ Hades '
             'ความสำเร็จที่ถูกส่งต่อในภาคใหม่ปรับเปลี่ยนตามยุคสมัยเข้ากับยุคปัจจุบัน แต่คงเอกลักษณ์ด้านเนื้อหาที่ชวนติดตามและระบบการเล่นแนวตะลุยดันเจี้ยนเต็มรูปแบบ')
    st.write('Download >> https://downloads.digitaltrends.com/diablo-iii/windows')

    st.write('2.Path Of Exile')
    st.markdown('![image](https://i.pinimg.com/736x/dc/ba/0b/dcba0be9ce870663790b01401f0fbca3.jpg)')
    st.write('Path Of Exile อีกหนึ่งเกมคุณภาพเล่นฟรีที่ได้รับการยกย่องจากแฟนซีรี่ย์เกม Diablo ทั่วโลก ด้วยรูปแบบเกมแนว Dungeon Crawler ตะลุยดันเจี้ยนในโลกแห่งความมืดเหนือจินตนาการ '
             'ถือเป็นเกมที่ประสบความสำเร็จนับตั้งแต่เปิดให้บริการครั้งแรกในปี 2013 ปัจจุบันมีการเปิดตัวเนื้อหาเสริมแทบทุกปีรวมถึงฟีเจอร์ใหม่ๆ ให้คุณเพลิดเพลินต่อไปตราบใดที่ยังไม่ได้เห็น Diablo 4')
    st.write('Download >> https://www.pathofexile.com/download')

    st.write("3.The Binding Of Isaac")
    st.markdown('![image](https://i.pinimg.com/564x/d2/06/a9/d206a938daa5c145169e0e4b79f0fe46.jpg)')
    st.write('The Binding Of Isaac ไม่ใช่เกมแนว hack n slash บู๊ล้างผลาญ แต่เป็นเกมแนว dungeon crawler ที่ประสบความสำเร็จมากที่สุด'
             ' แม้เนื้อเรื่องของเกมค่อนข้างรุนแรงบอกเล่าถึงความศรัทธาและการบูชายัญ'
             ' โดยผู้เล่นรับบทเป็นเด็กน้อยเคราะห์ร้ายจากเหตุการณ์ในครั้งนี้เพื่อหนีเอาชีวิตรอดจากชั้นใต้ดินของบ้านคล้ายดันเจี้ยนที่เต็มไปด้วยภัยอันตรายมากมาย')
    st.write('Download >> https://store.steampowered.com/app/113200/The_Binding_of_Isaac/')

    st.write('4.Darkest Dungeon')
    st.markdown('![image](https://i.pinimg.com/564x/a0/0f/02/a00f02acefd8e17fa3eeb74e8dfa45ad.jpg)')
    st.write('แม้จะมีกระแสข่าวกำลังทำภาค 2 แต่ตัวเกมภาคต้น Darkest Dungeon ยังคงมอบความตื่นเต้นชวนสยองท่ามกลางการเดินทางฝ่าคุกใต้ดินอันมืดมิดที่เต็มไปด้วยความสิ้นหวังแสดงออกผ่านสภาพจิตใจของตัวละครแต่ละตัว '
             'ซึ่งส่งผลกระทบต่อการต่อสู้อย่างหลีกเลี่ยงไม่ได้ อย่างไรก็ตามด้วยความที่ตัวเกมใช้ระบบต่อสู้แบบ Turn-based RPG ผู้เล่นจึงมีเวลาตัดสินใจก่อนทำสิ่งต่างๆ อาจจะเป็นเกมที่มอบความสนุกและความเครียดได้ในเวลาเดียวกัน')
    st.write('Download >> https://store.steampowered.com/app/262060/Darkest_Dungeon/')


    st.write('5.Enter The Gungeon')
    st.markdown('![image](https://i.pinimg.com/564x/f1/69/9d/f1699da21878a56a151f088185dd7310.jpg)')
    st.write('Enter The Gungeon เกมอินดี้แนว dungeon crawler หน้าตาดูธรรมดาแต่เล่นโคตรยากคล้ายซีรี่ย์เกม Dark Souls '
             'ตัวละครมีปืนเป็นอาวุธหลักและมีให้เลือกใช้หลากหลายรูปแบบในสถานการณ์ที่กำลังเผชิญ แต่ไม่ใช่การเดินหน้ายิงแหลกเหมือนเกมทั่วๆไป '
             'เพราะผู้เล่นต้องใช้ฝีมือหลบหลีกการโจมตีจากศัตรูไม่ว่าจะเป็นมอนสเตอร์ทั่วไปรวมถึงบอสประจำด่านนั้นๆ ซึ่งความยากระดับทำให้คนเล่นหัวร้อนได้ตลอดเวลาจึงเป็นเกมที่เล่นสนุกไม่มีเบื่อ')
    st.write('Download >> https://gogunlocked.com/enter-the-gungeon-free-download/')
