import streamlit as st
import numpy as np

st.set_page_config(page_title="Cobb 500 Pro Manager", layout="wide")

# القائمة الجانبية المتقدمة
st.sidebar.title("🛠️ لوحة التحكم الاحترافية")
mode = st.sidebar.selectbox("اختر المهمة:", ["تحليل التجانس", "تشخيص الأصوات (السماعة)", "جدول الإظلام والتهوية", "حاسبة الربح الصافي"])

# 1. تحليل التجانس
if mode == "تحليل التجانس":
    st.header("⚖️ اختبار تجانس القطيع")
    st.write("زن 10 كتاكيت عشوائية من أقفاص مختلفة وأدخل أوزانهم بالجرام:")
    
    weights = []
    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            w = st.number_input(f"طائر {i+1}", min_value=40, max_value=4000, value=500, key=f"w{i}")
            weights.append(w)
    
    if st.button("تحليل البيانات"):
        avg = np.mean(weights)
        std_dev = np.std(weights)
        # حساب التجانس (كم طائر يقع ضمن +/- 10% من المتوسط)
        upper = avg * 1.10
        lower = avg * 0.90
        within_range = [w for w in weights if lower <= w <= upper]
        uniformity = (len(within_range) / 10) * 100
        
        st.metric("متوسط الوزن", f"{avg:.1f} جم")
        st.metric("نسبة التجانس", f"{uniformity}%")
        
        if uniformity >= 80:
            st.success("✅ تجانس ممتاز! توزيع العلف والحرارة مثالي.")
        else:
            st.error("⚠️ تجانس ضعيف! ابحث عن 'السردة' أو تأكد من وصول الماء للجميع في البطارية.")

# 2. تشخيص الأصوات عبر السماعة
elif mode == "تشخيص الأصوات (السماعة)":
    st.header("🎧 غرفة التنصت الحيوية")
    st.info("ضع سماعة البلوتوث داخل البطارية في وقت السكون (الإظلام) واستمع:")
    
    sound_diag = {
        "الصوت المسموع": ["خروشة/عطسة متقطعة", "صوت ضفادع (نكررة)", "صراخ حاد ومستمر", "صمت تام مع لهث"],
        "التشخيص المحتمل": ["بداية برد (مايكوبلازما)", "إصابة تنفسية شديدة / نيوموكاسل", "جوع أو برد شديد", "إجهاد حراري (الحرارة مرتفعة جداً)"],
        "الإجراء الفوري": ["موسع شعب + تيلوزين", "تدخل بيطري فوري + رافع مناعة", "تأكد من الدفايات والعلف", "شغل الشفاطات فوراً"]
    }
    st.table(sound_diag)

# 3. جدول الإظلام (سر نجاح كوب 500)
elif mode == "جدول الإظلام والتهوية":
    st.header("🌑 برنامج الإضاءة والإظلام")
    st.write("سلالة كوب 500 تحتاج إظلام لتقوية الجهاز الدوري ومنع الاستسقاء:")
    
    light_data = {
        "العمر (يوم)": ["1-7", "8-21", "22-30", "31-الذبح"],
        "ساعات الإظلام": ["1 ساعة (تعود)", "4-6 ساعات", "3 ساعات", "1 ساعة"],
        "الهدف": ["تأسيس", "بناء القلب والعظام", "زيادة سحب العلف", "دفع الوزن النهائي"]
    }
    st.table(light_data)
    st.warning("⚠️ في البطاريات، تأكد أن شدة الإضاءة متساوية في جميع الأدوار (العلوي والسفلي).")

# 4. حاسبة الربح الصافي
elif mode == "حاسبة الربح الصافي":
    st.header("💰 حاسبة الجدوى الاقتصادية")
    col1, col2 = st.columns(2)
    with col1:
        total_birds = st.number_input("عدد الكتاكيت عند الاستلام:", value=100)
        mortality = st.number_input("عدد النافق (الميت):", value=5)
        chick_price = st.number_input("سعر الكتكوت:", value=30.0)
    with col2:
        feed_price = st.number_input("سعر طن العلف:", value=25000.0)
        selling_price = st.number_input("سعر كيلو اللحم عند البيع:", value=80.0)
        avg_final_weight = st.number_input("متوسط الوزن عند البيع (كيلو):", value=2.2)

    if st.button("احسب الأرباح"):
        live_birds = total_birds - mortality
        total_meat = live_birds * avg_final_weight
        total_income = total_meat * selling_price
        # حساب التكلفة (علف + كتكوت + 10% نثريات)
        feed_cost = (live_birds * 4.2 * (feed_price/1000))
        total_expenses = feed_cost + (total_birds * chick_price)
        total_expenses *= 1.10 # إضافة 10% كهرباء وأدوية
        
        profit = total_income - total_expenses
        
        st.metric("إجمالي الدخل", f"{total_income:,.0f}")
        st.metric("صافي الربح التقديري", f"{profit:,.0f}", delta=f"{int(profit/total_birds)} لكل طائر")
