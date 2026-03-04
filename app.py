import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="مدير مزرعة كوب 500", page_icon="🐥", layout="wide")

# دالة لحفظ البيانات في ملف سجل
def save_data(date, weight, birds_count, notes):
    try:
        new_data = pd.DataFrame([[date, weight, birds_count, notes]], 
                                columns=['التاريخ', 'الوزن', 'العدد', 'ملاحظات'])
        new_data.to_csv('farm_records.csv', mode='a', header=not pd.io.common.file_exists('farm_records.csv'), index=False)
        return True
    except:
        return False

# القائمة الجانبية
st.sidebar.title("🛠️ لوحة التحكم")
menu = st.sidebar.radio("اختر القسم:", 
    ["📝 سجل اليومية", "⚖️ تحليل التجانس", "🎧 مراقبة السماعة", "💰 حساب الأرباح", "📖 دليل كوب 500"])

# 1. سجل اليومية
if menu == "📝 سجل اليومية":
    st.header("📝 تسجيل البيانات اليومية للبطارية")
    col1, col2 = st.columns(2)
    with col1:
        date_in = st.date_input("تاريخ اليوم", datetime.now())
        weight_in = st.number_input("متوسط الوزن الحالي (جرام):", min_value=40, value=500)
    with col2:
        birds_in = st.number_input("العدد المتبقي في البطارية:", min_value=1, value=100)
        notes_in = st.text_area("ملاحظات (الأدوية، التهوية، النفوق):")

    if st.button("حفظ القراءة في السجل"):
        if save_data(date_in, weight_in, birds_in, notes_in):
            st.success("✅ تم حفظ البيانات بنجاح في سجل الهاتف!")
        
    st.markdown("---")
    st.subheader("📊 عرض السجلات السابقة")
    try:
        df = pd.read_csv('farm_records.csv')
        st.dataframe(df.tail(10)) # عرض آخر 10 أيام
    except:
        st.info("لا توجد سجلات محفوظة بعد.")

# 2. تحليل التجانس
elif menu == "⚖️ تحليل التجانس":
    st.header("⚖️ اختبار تجانس أوزان القطيع")
    st.info("زن 10 كتاكيت عشوائية من مستويات مختلفة في البطارية وأدخل أوزانهم:")
    
    weights = []
    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            w = st.number_input(f"طائر {i+1}", min_value=40, max_value=5000, value=500, key=f"w{i}")
            weights.append(w)
    
    if st.button("تحليل التجانس الآن"):
        avg = np.mean(weights)
        upper = avg * 1.10
        lower = avg * 0.90
        within_range = [w for w in weights if lower <= w <= upper]
        uniformity = (len(within_range) / 10) * 100
        
        st.metric("متوسط وزن القطيع", f"{avg:.1f} جرام")
        if uniformity >= 85:
            st.success(f"نسبة التجانس: {uniformity}% - ممتاز جداً!")
        elif uniformity >= 70:
            st.warning(f"نسبة التجانس: {uniformity}% - مقبول (راجع توزيع العلف).")
        else:
            st.error(f"نسبة التجانس: {uniformity}% - ضعيف! (توجد سرده كثيرة).")

# 3. مراقبة السماعة
elif menu == "🎧 مراقبة السماعة":
    st.header("🎧 دليل تحليل الأصوات (سماعة البلوتوث)")
    st.markdown("""
    **كيفية الاستخدام:**
    1. اربط سماعة البلوتوث بهاتفك.
    2. ضع سماعة واحدة بجانب فتحات التهوية في البطارية.
    3. استمع في وقت السكون (الإظلام) وقارن بما يلي:
    """)
    
    sound_table = {
        "الصوت المسموع": ["عطسة خفيفة (تزييق)", "صوت ضفادع (نكررة)", "زقزقة حادة وعالية", "صمت مع نهجان"],
        "التشخيص": ["بداية إصابة تنفسية", "إصابة شديدة (نيوكاسل/آي بي)", "برد أو جوع", "إجهاد حراري شديد"],
        "الإجراء المقترح": ["موسع شعب + تيلوزين", "تحصين اضطراري + رافع مناعة", "رفع الحرارة فوراً", "تشغيل الشفاطات + فيتامين C"]
    }
    st.table(sound_table)

# 4. حساب الأرباح
elif menu == "💰 حساب الأرباح":
    st.header("💰 حاسبة المكسب الصافي")
    c1, c2 = st.columns(2)
    with c1:
        total_birds = st.number_input("عدد الكتاكيت المستلمة:", value=100)
        chick_cost = st.number_input("سعر الكتكوت الواحد:", value=35.0)
        feed_price_ton = st.number_input("سعر طن العلف (بالعملة):", value=28000.0)
    with c2:
        meat_price = st.number_input("سعر كيلو اللحم (بيع):", value=85.0)
        dead_birds = st.number_input("عدد النافق:", value=5)
        other_costs = st.number_input("مصاريف أخرى (كهرباء، دواء):", value=500.0)

    if st.button("حساب الأرباح التقديرية"):
        live_birds = total_birds - dead_birds
        # استهلاك العلف التقريبي لكوب 500 هو 4 كيلو للوصول لوزن 2.2 كيلو
        total_feed_tons = (live_birds * 4) / 1000
        total_expenses = (total_birds * chick_cost) + (total_feed_tons * feed_price_ton) + other_costs
        total_income = (live_birds * 2.2) * meat_price
        net_profit = total_income - total_expenses
        
        st.metric("إجمالي الدخل", f"{total_income:,.2f}")
        st.metric("إجمالي التكاليف", f"{total_expenses:,.2f}")
        st.metric("صافي الربح", f"{net_profit:,.2f}", delta_color="normal")

# 5. دليل كوب 500
elif menu == "📖 دليل كوب 500":
    st.header("📖 نصائح ذهبية لنظام البطاريات")
    st.write("""
    - **التهوية:** في البطاريات، غاز الأمونيا يتركز في الأدوار السفلية. تأكد من وجود شفاط قوي.
    - **الماء:** تأكد من عمل 'النيبل' يومياً، انسداد واحدة قد يقتل 10 كتاكيت عطشاً.
    - **الإظلام:** كوب 500 ينمو بسرعة أكبر من قلبه، الإظلام لمدة 4-6 ساعات يومياً يحميه من السكتة القلبية.
    - **النظافة:** ميزة البطارية هي عدم وجود فرشة، تأكد من سحب أدراج السبلكة كل يومين.
    """)

st.sidebar.markdown("---")
st.sidebar.info("صمم هذا التطبيق لمربي كوب 500 المحترفين 🚀")
