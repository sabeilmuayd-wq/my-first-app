import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="مدير مزرعة كوب 500", page_icon="🐥", layout="centered")

# تنسيق مخصص CSS لتحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #27ae60; color: white; }
    .report-card { background-color: #ffffff; padding: 20px; border-radius: 15px; border-right: 5px solid #27ae60; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🐥 نظام إدارة تسمين كوب 500")
st.subheader("نظام البطاريات - بروتوكول جيزوب وستيرمر")

# مدخلات المستخدم في القائمة الجانبية
with st.sidebar:
    st.header("⚙️ الإعدادات")
    count = st.number_input("عدد الكتاكيت:", min_value=1, value=100)
    age = st.slider("عمر الكتكوت (بالأيام):", 1, 45, 6)
    chick_price = st.number_input("سعر الكتكوت الواحد:", value=30.0)
    feed_price = st.number_input("سعر طن العلف (بالجنيه):", value=25000)

# الحسابات المنطقية لسلالة كوب 500
if age <= 7:
    target_weight = 42 + (age * 24)
    daily_feed = (20 + (age * 2)) * count / 1000
    temp = 33 - (2 if age > 3 else 0)
    protocol = "🛡️ **فترة الاستقبال:** استخدم **ستيرمر (Steermer)** 1سم/لتر لرفع المناعة."
else:
    target_weight = 200 + ((age - 7) * 65)
    daily_feed = (50 + ((age - 7) * 12)) * count / 1000
    temp = 28 - (3 if age > 14 else 0)
    protocol = "🚀 **فترة التحويل:** استخدم **جيزوب (Gezob)** 1سم/لتر لزيادة وزن الصدر."

# مفكرة الأعشاب
herbs = {
    1: "محلول جفاف أو ماء بسكر",
    4: "زنجبيل دافئ (منشط دورة دموية)",
    5: "نعناع مغلي (موسع شعب)",
    6: "🌿 **الكركم:** ملعقة على العلف (أهم عشب لليوم السادس)",
    7: "خل أبيض 5% لغسيل الكلى",
    10: "ثوم وبصل بودرة (مضاد حيوي طبيعي)",
    15: "زعتر (للوقاية من الكوكسيديا)"
}
today_herb = herbs.get(age, "إضافة الكركم أو النعناع للوقاية العامة")

# عرض النتائج
col1, col2, col3 = st.columns(3)
col1.metric("الوزن المستهدف", f"{target_weight} جرام")
col2.metric("علف اليوم", f"{daily_feed:.1f} كجم")
col3.metric("الحرارة", f"{temp} °م")

st.markdown("---")

with st.container():
    st.markdown(f"""
    <div class="report-card">
        <h3>📅 تقرير اليوم {age}</h3>
        <p><b>💊 البروتوكول الطبي:</b> {protocol}</p>
        <p><b>🌿 عشب اليوم:</b> {today_herb}</p>
        <p style='color: #e67e22;'>⚠️ <b>تنبيه البطارية:</b> تأكد من فحص ضغط مياه النيبل وتنظيف السبلة.</p>
    </div>
    """, unsafe_allow_html=True)

# جدول البيانات المتوقع للدورة كاملة (رسم بياني)
st.markdown("### 📈 منحنى النمو المتوقع")
chart_data = pd.DataFrame({
    'اليوم': range(1, 41),
    'الوزن المتوقع (جرام)': [42 + (i * 24) if i <= 7 else 200 + ((i - 7) * 65) for i in range(1, 41)]
})
st.line_chart(chart_data.set_index('اليوم'))

# حسابات مالية سريعة
st.markdown("### 💰 تقدير التكاليف")
total_feed_est = (daily_feed * age * 0.7) # تقدير تقريبي
cost_chicks = count * chick_price
cost_feed = (total_feed_est * feed_price / 1000)
st.write(f"تكلفة الكتاكيت: **{cost_chicks:,.0f}**")
st.write(f"تكلفة العلف التقريبية حتى اليوم: **{cost_feed:,.0f}**")

st.info("هذا التطبيق مبرمج خصيصاً لسلالة كوب 500 بناءً على كتالوج الشركة المصنعة.")
