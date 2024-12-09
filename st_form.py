import streamlit as st

st.title('st.form')

# 'with' 표기법을 사용한 전체 예시
with st.form('my_form'):
    st.subheader('**개인정보 입력하기**')

    # 입력 위젯
    selectage = st.selectbox('나이를 입력하시오', ['0-9', '10-19','20-29','30-'])
    selectgender = st.selectbox('성별을 선택하시오.', ['남', '여', '비밀'])
    selectstudent = st.selectbox('학생이십니까?', ['초등학생', '중학생', '고등학생', '대학생', '그 외'])
    selectmilitary = st.selectbox('군필이십니까?(여자면 선택안해도됨)', ['군필', '미필', '면제'])
    owngain_val = st.checkbox('자신의 개정 가져오기')

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        입력하신 내용:
        - 나이: `{selectage}`
        - 성별: `{selectgender}`
        - 학생: `{selectstudent}`
        - 군필 여부: `{selectmilitary}`
        - 자신의 개정: `{owngain_val}`
        ''')    

