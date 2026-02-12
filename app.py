import streamlit as st


st.set_page_config(page_title="Образователна викторина", page_icon="📚")


st.title("📚 Образователна викторина")
st.write("Отговорете на въпросите по География и История")


if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = {}


questions = {
    "q1": {
        "question": "Коя е столицата на България?",
        "options": ["Пловдив", "София", "Варна", "Бургас"],
        "correct": "София",
        "category": "География"
    },
    "q2": {
        "question": "Коя е най-дългата река в България?",
        "options": ["Марица", "Дунав", "Искър", "Струма"],
        "correct": "Искър",
        "category": "География"
    },
    "q3": {
        "question": "През коя година България получава независимост от Османската империя?",
        "options": ["1876", "1878", "1908", "1912"],
        "correct": "1908",
        "category": "История"
    },
    "q4": {
        "question": "Кой е основателят на Българската държава?",
        "options": ["Хан Аспарух", "Хан Крум", "Цар Симеон", "Хан Тервел"],
        "correct": "Хан Аспарух",
        "category": "История"
    },
    "q5": {
        "question": "Коя планина е най-висока в България?",
        "options": ["Витоша", "Пирин", "Рила", "Стара планина"],
        "correct": "Рила",
        "category": "География"
    },
    "q6": {
        "question": "Коя е фамилията на Сашо?",
        "options": ["Видев", "Владев", "Ликов", "Христов"],
        "correct": "Видев",
        "category": "Сашо"
    },
 "q7": {
        "question": "Колко е висок Сашо?",
        "options": ["175см", "140см", "190см", "178см"],
        "correct": "175см",
        "category": "Сашо"
    },
 "q8": {
        "question": "В кой квартал живее Сашо?",
        "options": ["Мараша", "Смирненски", "Тракия", "Център"],
        "correct": "Мараша",
        "category": "Сашо"
    },
"q9": {
        "question": "На кой етаж живее Сашо?",
        "options": ["2ри", "3ти", "7ми", "14ти"],
        "correct": "2ри",
        "category": "Сашо"
    },
}


with st.form("quiz_form"):
    st.subheader("Отговорете на следните въпроси:")
    
    user_answers = {}
    
    for q_id, q_data in questions.items():
        st.markdown(f"**{q_data['category']}**")
        user_answers[q_id] = st.radio(
            q_data['question'],
            options=q_data['options'],
            key=q_id
        )
        st.markdown("---")
    
   
    submit_button = st.form_submit_button("✅ Изпрати отговорите")


if submit_button:
    st.session_state.submitted = True
    st.session_state.answers = user_answers
    
   
    correct_count = 0
    total_questions = len(questions)
    
    st.subheader("📊 Резултати:")
    
    for q_id, q_data in questions.items():
        user_answer = st.session_state.answers[q_id]
        correct_answer = q_data['correct']
        
        if user_answer == correct_answer:
            correct_count += 1
            st.success(f"✅ {q_data['question']}")
            st.write(f"Вашият отговор: **{user_answer}** - Верен!")
        else:
            st.error(f"❌ {q_data['question']}")
            st.write(f"Вашият отговор: **{user_answer}**")
            st.write(f"Верен отговор: **{correct_answer}**")
        
        st.markdown("---")
    
    
    percentage = (correct_count / total_questions) * 100
    
    st.subheader("🎯 Крайна оценка:")
    st.metric(label="Верни отговори", value=f"{correct_count}/{total_questions}")
    st.progress(percentage / 100)
    
    if percentage == 100:
        st.balloons()
        st.success("🎉 Браво! Отговорихте правилно на всички въпроси!")
    elif percentage >= 70:
        st.success(f"👍 Много добре! Успехът ви е {percentage:.0f}%")
    elif percentage >= 50:
        st.warning(f"📖 Добре, но има място за подобрение. Успехът ви е {percentage:.0f}%")
    else:
        st.error(f"📚 Трябва да учите повече. Успехът ви е {percentage:.0f}%")
    
   
    if st.button("🔄 Опитай отново"):
        st.session_state.submitted = False
        st.session_state.answers = {}
        st.rerun()


if not st.session_state.submitted:
    with st.sidebar:
        st.header("ℹ️ Инструкции")
        st.write("""
        1. Прочетете внимателно всеки въпрос
        2. Изберете един отговор за всеки въпрос
        3. Натиснете бутона "Изпрати отговорите"
        4. Вижте резултатите си
        """)
        
        st.header("📋 Категории")
        st.write("- География")
        st.write("- История")
