<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مساعد التسمين الذكي - كوب 500</title>
    <style>
        :root {
            --primary: #2c3e50;
            --secondary: #27ae60;
            --accent: #e67e22;
            --bg: #f8f9fa;
        }
        body { font-family: 'Segoe UI', sans-serif; background-color: var(--bg); margin: 0; padding: 15px; text-align: center; }
        .container { max-width: 550px; margin: auto; background: white; padding: 20px; border-radius: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); }
        h1 { color: var(--primary); font-size: 1.4rem; margin-bottom: 20px; border-bottom: 3px solid var(--secondary); display: inline-block; padding-bottom: 5px; }
        .input-group { background: #fdfdfd; padding: 15px; border-radius: 15px; margin-bottom: 20px; border: 1px solid #eee; }
        label { display: block; margin-bottom: 8px; font-weight: bold; color: var(--primary); }
        input { width: 90%; padding: 12px; border-radius: 10px; border: 1px solid #ccc; font-size: 1rem; text-align: center; }
        button { width: 100%; background: var(--secondary); color: white; border: none; padding: 15px; border-radius: 12px; font-size: 1.1rem; cursor: pointer; font-weight: bold; margin-top: 10px; }
        
        .result-area { display: none; margin-top: 25px; text-align: right; }
        .section { background: #fff; padding: 15px; border-radius: 15px; margin-bottom: 15px; border-right: 5px solid var(--secondary); box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .herb-section { border-right-color: var(--accent); background: #fff8f0; }
        .med-section { border-right-color: #3498db; background: #f0f7ff; }
        
        .highlight { color: var(--secondary); font-weight: bold; }
        .day-badge { background: var(--primary); color: white; padding: 2px 10px; border-radius: 10px; font-size: 0.9rem; }
        table { width: 100%; margin-top: 10px; font-size: 0.85rem; border-collapse: collapse; }
        th, td { border: 1px solid #eee; padding: 8px; text-align: center; }
    </style>
</head>
<body>

<div class="container">
    <h1>دليل كتاكيت كوب 500 🐥</h1>
    
    <div class="input-group">
        <label>عدد الكتاكيت في البطاريات:</label>
        <input type="number" id="count" placeholder="مثلاً: 100">
        <label>عمر الكتكوت الحالي (أيام):</label>
        <input type="number" id="age" placeholder="يوم">
        <button onclick="updateApp()">عرض الجدول اليومي</button>
    </div>

    <div id="mainResult" class="result-area">
        <div class="section">
            <h3>📊 حالة النمو اليوم <span class="day-badge" id="dayDisplay"></span></h3>
            <p>📍 الوزن المستهدف: <span class="highlight" id="w"></span> جرام</p>
            <p>📍 علف القطيع اليومي: <span class="highlight" id="f"></span> كجم</p>
            <p>📍 حرارة البطارية: <span class="highlight" id="t"></span> °م</p>
        </div>

        <div class="section med-section">
            <h3>💊 برنامج (ستيرمر & جيزوب)</h3>
            <p id="medAdvice"></p>
        </div>

        <div class="section herb-section">
            <h3>🌿 مفكرة الأعشاب الطبيعية</h3>
            <p id="herbAdvice"></p>
            <p><small>* ملحوظة: الأعشاب مكملة ولا تغني عن التحصينات.</small></p>
        </div>
    </div>
</div>

<script>
    function updateApp() {
        const age = parseInt(document.getElementById('age').value);
        const count = parseInt(document.getElementById('count').value);
        if(!age || !count) return alert("أدخل البيانات");

        let weight, feed, temp, med, herb;

        // 1. حسابات النمو والحرارة
        if(age <= 7) {
            weight = 40 + (age * 22);
            feed = (18 + (age * 3)) * count / 1000;
            temp = 33 - (age > 3 ? 2 : 0);
            med = "استخدم <b>ستيرمر (Steermer)</b> الآن: ممتاز لتقوية المناعة الأولية ومنع الصدمات.";
        } else {
            weight = 200 + ((age-7) * 60);
            feed = (50 + ((age-7) * 10)) * count / 1000;
            temp = 28 - (age > 14 ? 3 : 0);
            med = "وقت الـ <b>جيزوب (Gezob)</b>: أضف 1سم/لتر لزيادة تحويل اللحم في الصدر.";
        }

        // 2. مفكرة الأعشاب اليومية
        const herbTable = {
            1: "ماء بسكر أو محلول جفاف فقط.",
            2: "شاي مغلي خفيف (لمنع الإسهال).",
            3: "شاي مغلي خفيف.",
            4: "زنجبيل (منشط دورة دموية).",
            5: "نعناع مغلي (موسع شعب هوائية).",
            6: "<b>الكركم:</b> ملعقة على العلف (مضاد التهاب وفتح شهية).",
            7: "خل 5% (2سم/لتر) لغسيل الكلى.",
            10: "ثوم وبصل بودرة على العلف.",
            14: "زعتر مغلي (مضاد حيوي تنفسي طبيعي)."
        };

        herb = herbTable[age] || "استخدم الكركم أو النعناع كإضافة وقائية.";

        // عرض النتائج
        document.getElementById('dayDisplay').innerText = "يوم " + age;
        document.getElementById('w').innerText = weight;
        document.getElementById('f').innerText = feed.toFixed(1);
        document.getElementById('t').innerText = temp;
        document.getElementById('medAdvice').innerHTML = med;
        document.getElementById('herbAdvice').innerHTML = "<b>اليوم ينصح بـ:</b> " + herb;
        
        document.getElementById('mainResult').style.display = "block";
    }
</script>

</body>
</html>
