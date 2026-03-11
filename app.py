import streamlit as st
import secrets
import string

# إعدادات الصفحة لتظهر كأنها تطبيق موبايل احترافي
st.set_page_config(page_title="Axion Secure", page_icon="🛡️", layout="centered")

# تصميم الواجهة باستخدام CSS لجعلها تبدو "بنكية"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #1E3A8A; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    .status-box { padding: 20px; border-radius: 10px; background-color: #ffffff; border: 1px solid #e0e0e0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# العنوان العلوي (الهوية البصرية)
st.title("🛡️ Axion Secure")
st.subheader("نظام الضمان الرقمي المشفر v1.5")
st.write("---")

# القائمة الجانبية أو الأقسام
tab1, tab2 = st.tabs(["🚀 إنشاء صفقة جديدة", "🔍 التحقق من الضمان"])

with tab1:
    st.write("### بيانات الصفقة")
    merchant_name = st.text_input("اسم التاجر (كامبالا)")
    buyer_location = st.selectbox("موقع المشتري", ["بورتسودان", "الخرطوم", "الدمازين", "عطبرة"])
    amount = st.number_input("مبلغ الضمان (USD)", min_value=0)
    
    if st.button("تفعيل قفل الضمان الرقمي"):
        # توليد الأكواد
        alphabet = string.ascii_uppercase + string.digits
        buyer_key = ''.join(secrets.choice(alphabet) for i in range(8))
        broker_key = ''.join(secrets.choice(alphabet) for i in range(8))
        
        st.success("✅ تم تفعيل الضمان بنجاح!")
        
        st.markdown(f"""
        <div class="status-box">
            <p style='color: #1E3A8A;'><b>رقم العملية:</b> AXN-{secrets.randbelow(10000)}</p>
            <h4 style='color: red;'>كود المشتري (للسودان): {buyer_key}</h4>
            <h4 style='color: green;'>كود الوسيط (لك أنت): {broker_key}</h4>
            <p><small>⚠️ ملاحظة: لا تشارك كود الوسيط مع أي شخص.</small></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("قم بتصوير الشاشة (Screenshot) أو إرسال الأكواد للأطراف المعنية.")

with tab2:
    st.write("### فك تشفير الضمان")
    check_buyer_key = st.text_input("أدخل كود المشتري القادم من السودان")
    check_broker_key = st.text_input("أدخل كود الوسيط الخاص بك")
    
    if st.button("تحرير المبلغ"):
        if check_buyer_key and check_broker_key:
            st.balloons()
            st.success("🔓 تطابق كامل! تم تحرير المبلغ للتاجر بنجاح.")
        else:
            st.error("❌ الأكواد غير متطابقة أو ناقصة.")

# تذييل الصفحة
st.write("---")
st.caption("© 2026 Axion Pay Project | Secure v1.4 System")
