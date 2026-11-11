"""يبني ملف أعمال أكاديمية رزين (عربي: razeen/index.html، إنجليزي: razeen/en/index.html).
عدّلي المحتوى هنا ثم شغّلي:  python3 razeen/build.py"""
import html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from labs_section import section as labs_section, C as LABS_C

ROOT = pathlib.Path(__file__).resolve().parent
SITE = "https://razeen-academy.pages.dev"
E = html.escape

ICONS = {
  "lab": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/>',
  "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
  "path": '<path d="M4 19h4l3-7 3 4 2-5h4"/><circle cx="4" cy="19" r="1.5"/><circle cx="20" cy="11" r="1.5"/>',
  "cert": '<circle cx="12" cy="9" r="5"/><path d="M9 13.5 8 21l4-2 4 2-1-7.5"/>',
  "flag": '<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>',
  "trophy": '<path d="M8 4h8v5a4 4 0 0 1-8 0zM5 5H3v2a3 3 0 0 0 3 3M19 5h2v2a3 3 0 0 1-3 3M10 16h4M9 20h6M12 13v3"/>',
  "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a5 5 0 0 1 3.5 6"/>',
  "tent": '<path d="M3 20 12 4l9 16zM12 4v16M8.5 20 12 13l3.5 7"/>',
  "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
  "cloud": '<path d="M7 18a4 4 0 0 1-.6-8A5.5 5.5 0 0 1 17 8.5 4.5 4.5 0 0 1 17 18z"/>',
  "lang": '<path d="M4 5h9M8.5 3v2M6 5c0 4 3 7 6 8M11 5c0 4-3 7-6 8M13 21l4-10 4 10M14.5 17.5h5"/>',
}
def icon(k): return f'<div class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg></div>'

T = {}
T["ar"] = dict(
  dir="rtl", title="ملف أعمال أكاديمية رزين", desc="ملف أعمال أكاديمية رزين: من نحن، خدماتنا، الباقات والخصومات، وخطتنا للسنة القادمة وما نقدمه للأندية الطلابية والجامعات والشركات.",
  other="/razeen/en/", other_lbl="English", skip="تخطَّ إلى المحتوى", brand="أكاديمية رزين", brand_sub="PORTFOLIO · 2026",
  nav=[("#about", "عنّي"), ("#platform", "المنصة"), ("#services", "الخدمات"), ("#plans", "الباقات"), ("#roadmap", "الخطة"), ("#partners", "الشراكات")],
  visit="زيارة المنصة", badge="ملف أعمال · نوفمبر 2026",
  h1='الحوسبة السحابية بالعربي،<br><mark>بالتطبيق لا بالتلقين</mark>',
  lead="أكاديمية رزين منصة سعودية لتعلّم الحوسبة السحابية وأمنها عبر مختبرات وتحديات عملية في بيئات حقيقية، مرتبطة بالمعايير السعودية، ومن المستوى المبتدئ إلى الاحتراف.",
  cta1="جرّب المنصة مجانًا", cta2="تواصل معنا", print="تنزيل PDF",
  facts=[("15", "تخصصًا سحابيًا"), ("3", "مزوّدين: AWS وAzure وGoogle"), ("8", "مختبرات وتحديات مجانية منشورة"), ("4", "مستويات من المبتدئ للاحترافي"), ("2", "لغتان: العربية والإنجليزية")],
  # عنّي
  k_about="FILE-01 · FOUNDER", h_about="عن المؤسِّسة",
  name="رزان العوفي", role="مؤسِّسة أكاديمية رزين · أخصائية حوسبة سحابية",
  dl=[("التخصص", "أخصائية حوسبة سحابية")],
  about_p=[
    "أعمل في الحوسبة السحابية بجميع تخصصاتها بشكل يومي: بناء البنية، وتأمينها، ومطابقتها مع ضوابط الأمن السيبراني للحوسبة السحابية (NCA CCC) ونظام حماية البيانات الشخصية (PDPL).",
    "لاحظت أن أغلب المحتوى العملي في السحابة مكتوب بالإنجليزية، وأن كثيرًا من المتعلمين يدرسون النظريات بدون أن يلمسوا بيئة حقيقية، وبدون ربطها بالأنظمة التي تُطبَّق فعلًا في السعودية.",
    "بنيت رزين لتسدّ هذه الفجوة: مختبرات تحلّها بيدك، بلغة تفهمها، وكل ثغرة فيها مرتبطة بالضابط الذي تخالفه.",
  ],
  quote="هدفي أن يتخرج المتدرب من رزين وقد طبّق ما تعلّمه فعلًا، لا أن يحفظه فقط.",
  # المنصة
  k_plat="FILE-02 · PLATFORM", h_plat="عن المنصة", p_plat="رزين أقرب إلى منصة تحديات عملية منها إلى دورة تدريبية: تتعلم بحل سيناريوهات تحاكي حوادث حقيقية في شركات خيالية.",
  why=[("cloud", "تطبيق عملي في بيئة حقيقية", "تكتشف الثغرة بنفسك على خدمات سحابية فعلية، والخادم يتحقق من إجابتك، ولا يُحتسب لك إلا ما حللته فعلًا."),
       ("shield", "مرتبطة بالمعايير السعودية", "كل مختبر يربط الثغرة بالضابط الذي تخالفه في NCA CCC وPDPL، وتظهر لك نسبة إتقانك لكل ضابط مع شرح له."),
       ("lang", "بالعربية أولًا", "الشرح والأسئلة والتلميحات بالعربية، مع المصطلحات التقنية كما تراها في عملك، ونسخة إنجليزية كاملة للمنصة.")],
  journey_h="رحلة المتدرب في كل مستوى", journey=[("LEARN", "تعلّم", "مختبرات تشرح المفهوم وتطبّقه خطوة بخطوة."), ("PRACTICE", "تدرّب", "تحديات يومية قصيرة تثبّت ما تعلّمته."), ("PROVE", "أثبت مهارتك", "تحديات CTF وشهادة عند إكمال المسار كاملًا.")],
  specs_h="التخصصات الخمسة عشر",
  groups=[("الأساسيات ومزوّدو السحابة", ["أساسيات الحوسبة السحابية", "AWS", "Microsoft Azure", "Google Cloud"]),
          ("الهندسة والتشغيل", ["معمارية السحابة وهندستها", "DevOps والتكامل والنشر المستمر", "الحاويات وKubernetes", "البنية التحتية كشيفرة", "شبكات السحابة", "قواعد البيانات والتخزين", "المراقبة والتشغيل", "تحسين التكلفة"]),
          ("الأمن والبيانات", ["أمن السحابة وSOC", "CTF والتحديات الأمنية", "البيانات والذكاء الاصطناعي في السحابة"])],
  specs_note="كل تخصص مخطط له على المزودين الثلاثة. المتاح الآن: مسار AWS للمبتدئين، والباقي يُنشر تباعًا حسب الخطة أدناه.",
  # الخدمات
  k_srv="FILE-03 · SERVICES", h_srv="الخدمات المقدَّمة", p_srv="الحالة بجانب كل خدمة حقيقية: «متاح الآن» يعني أنه يعمل اليوم على المنصة.",
  now="متاح الآن", soon="قريبًا", plan="ضمن الخطة",
  services=[("lab", "المختبرات العملية", "now", "سيناريوهات حوادث سحابية تحلّها خطوة بخطوة. ثلاثة مختبرات مجانية على AWS متاحة الآن، والمختبرات المتوسطة والمتقدمة ضمن الاشتراك."),
            ("cal", "التحديات اليومية", "now", "سلسلة تحديات قصيرة للمبتدئين على AWS، مجانية لكل المسجلين، تحلّ كل يوم تحديًا جديدًا."),
            ("path", "المسارات والمستويات", "now", "أربعة مستويات (مبتدئ، متوسط، متقدم، احترافي) في كل تخصص، مع مسار مبتدئ مجاني بالكامل."),
            ("cert", "شهادات الإتمام", "now", "شهادة بالإنجليزية عند إكمال مسار كامل، يمكن لأي جهة التحقق منها من صفحة التحقق في المنصة."),
            ("trophy", "لوحة الصدارة وفعاليات CTF", "now", "لوحة صدارة عامة بالنقاط، وفعاليات CTF بلوحة مباشرة للجهات والمعسكرات، مثل فعالية معسكر Azure Cloud Security Camp مع إيجر."),
            ("tent", "المعسكرات التدريبية", "now", "معسكرات مكثفة بالتعاون مع الجهات المنظمة، تشمل مختبرات مخصصة ويومًا ختاميًا للتحدي."),
            ("users", "باقات الفرق", "soon", "مقاعد لموظفي الشركات أو طلاب الدفعة، مع لوحة لمسؤول الفريق وتقارير تقدّم قابلة للتصدير."),
            ("cloud", "جلسات البيئة الحقيقية", "soon", "بيئة سحابية معزولة لكل متدرب تُنشأ تلقائيًا وتُحذف بعد الجلسة، بدون أن يحتاج حسابًا سحابيًا خاصًا به.")],
  # لماذا الاشتراك
  k_why="FILE-04 · SUBSCRIBER BENEFITS", h_why="ماذا يحصل عليه المشترك؟", p_why="المستوى المبتدئ يبقى مجانيًا بالكامل مع حلوله وتلميحاته، والاشتراك يفتح لك ما بعده:",
  benefits=[("lab", "مختبرات المستوى المتوسط والمتقدم", "سيناريوهات أعمق تحاكي حوادث حقيقية في الشركات، حسب باقتك."),
            ("cloud", "بيئة سحابية حقيقية لك وحدك", "جلسات في بيئة معزولة (25 جلسة شهريًا في الأساسية و50 في الاحترافية)، بدون حساب سحابي خاص ولا بطاقة ائتمان.", "soon"),
            ("path", "محتوى جديد باستمرار", "مختبرات وتحديات جديدة تُضاف كل شهر على AWS وAzure وGoogle Cloud."),
            ("shield", "إتقان المعايير السعودية", "كل ثغرة مرتبطة بضوابط NCA CCC وPDPL، مع نسبة إتقانك لكل ضابط وشرح له."),
            ("cert", "شهادات إتمام قابلة للتحقق", "شهادة لكل مسار تكمله، يمكن لجهة التوظيف التحقق منها مباشرة."),
            ("trophy", "لوحة الصدارة والملف الشخصي", "نقاطك وإنجازاتك في لوحة الصدارة، وملف عام تشاركه مع جهات التوظيف."),
            ("flag", "فعاليات CTF والمعسكرات", "أولوية المشاركة في فعاليات رزين ومعسكراتها مع الجهات الشريكة."),
            ("users", "أسعار وخصومات للطلاب", "خصم الطلاب 25٪ على السنوي، وعرض المؤسسين لأول 100 مشترك.")],
  # الباقات
  k_plans="FILE-05 · PLANS", h_plans="الباقات والأسعار", p_plans="الأسعار بالريال السعودي. الاشتراك السنوي يوفّر حتى 29٪ مقارنة بالشهري.",
  th=["الباقة", "السعر", "المستويات", "جلسات البيئة الحقيقية", "مناسبة لـ"],
  plans=[("المجانية", "0", "", "المبتدئ مع الحلول والتلميحات", "—", "من يبدأ في السحابة"),
         ("الأساسية", "50", "شهريًا · أو 450 سنويًا", "المبتدئ + المتوسط", "25 جلسة شهريًا", "الطلاب والمتعلمين الذاتيين"),
         ("الاحترافية", "100", "شهريًا · أو 850 سنويًا", "المبتدئ + المتوسط + المتقدم", "50 جلسة شهريًا", "المختصين والمستعدين للشهادات"),
         ("الفرق", "80", "لكل مقعد شهريًا · أقل شيء 10 مقاعد", "مستويات الاحترافية لكل عضو", "حسب الباقة", "الشركات والجامعات والأندية"),
         ("المعسكرات", "2,500 – 4,000", "للمعسكر الواحد", "محتوى مخصص للمعسكر", "حسب الاتفاق", "الجهات المنظمة للمعسكرات")],
  plans_note="إلغاء التجديد يبقي الوصول حتى نهاية الفترة المدفوعة، وعند انتهاء الاشتراك يعود الحساب للمجانية مع الاحتفاظ بكل التقدّم والشهادات. فتح الدفع الإلكتروني للاشتراكات قريبًا.",
  disc_h="الخصومات",
  discounts=[("عرض المؤسسين", "لأول 100 مشترك فقط", "الأساسية السنوية بـ 270 ر.س بدل 450، والاحترافية السنوية بـ 510 ر.س بدل 850 (خصم 40٪)."),
             ("خصم الطلاب", "25٪ على السنوي", "لطلاب الجامعات بعد التحقق من البريد الجامعي، صالح لمدة سنة."),
             ("كوبونات الشركاء", "للأندية والفعاليات", "أكواد خصم خاصة لأعضاء الأندية الطلابية ومشاركي المعسكرات والفعاليات."),
             ("سياسة الخصم", "أفضل خصم واحد", "لا تُجمع الخصومات، ويُطبَّق تلقائيًا الخصم الأفضل للمتدرب، ويُحسب في الخادم فقط.")],
  # التوجه
  k_vis="FILE-06 · VISION", h_vis="التوجّه المستقبلي للمنصة",
  vis_lead="أن تكون رزين المنصة العربية الأولى للتطبيق العملي في الحوسبة السحابية، والجسر بين ما يتعلمه الطالب وما يحتاجه سوق العمل السعودي.",
  vision=[("cert", "قسائم وخصومات على الشهادات", "سأتواصل مع مزودي الخدمات السحابية (AWS وMicrosoft وGoogle Cloud) ومراكز الاختبار لتوفير قسائم (Vouchers) وخصومات على شهاداتهم المهنية لمشتركي رزين، فيكون التدريب والاختبار في مكان واحد."),
          ("cloud", "تغطية المزودين الثلاثة", "كل تخصص من الخمسة عشر على AWS وAzure وGoogle Cloud، ليقارن المتدرب بين المزودين ويختار ما يناسب سوقه."),
          ("path", "أقسام جديدة مثل المسار الوظيفي", "أقسام تربط ما يتعلمه المتدرب بالوظائف السحابية في السوق: المسار الوظيفي لكل تخصص، والمهارات والشهادات المطلوبة لكل دور."),
          ("users", "شراكات تعليمية", "برامج مستمرة مع الأندية الطلابية والجامعات والشركات، تشمل فعاليات CTF ومعسكرات ومقاعد للفرق.")],
  # الخطة
  k_road="FILE-07 · 12-MONTH PLAN", h_road="الخطة لمدة سنة", p_road="الخطة قابلة للتعديل حسب احتياج المتدربين والشركاء.",
  road=[("المرحلة 1", "الإطلاق التجاري", ["فتح الاشتراكات المدفوعة عبر بوابة دفع سعودية", "تفعيل عرض المؤسسين لأول 100 مشترك", "تشغيل البيئات المعزولة لكل متدرب"]),
        ("المرحلة 2", "التوسع للمزودين", ["إطلاق مسار Microsoft Azure", "أول مختبرات Google Cloud", "إطلاق برنامج الأندية الطلابية"]),
        ("المرحلة 3", "الشهادات والشركات", ["التواصل مع مزودي الخدمات السحابية للحصول على قسائم (Vouchers) وخصومات على الشهادات", "إطلاق المستوى المتقدم", "تفعيل باقات الفرق ولوحة الشركات", "معسكرات مع جهات تدريبية"]),
        ("المرحلة 4", "أقسام ومستويات جديدة", ["إضافة أقسام جديدة للموقع مثل المسار الوظيفي وغيرها", "إطلاق المستوى الاحترافي", "فعالية CTF سنوية مفتوحة باسم رزين", "تقرير سنوي بالأثر والإحصاءات"])],
  # الشراكات
  k_par="FILE-08 · PARTNERSHIPS", h_par="ما نقدّمه للأندية والجامعات والشركات",
  partners=[("STUDENT CLUBS", "الأندية الطلابية", ["استضافة فعاليات CTF مجانًا مع لوحة صدارة مباشرة", "كوبون خصم خاص لأعضاء النادي", "ورش عمل عملية مشتركة على المنصة", "إبراز النادي كشريك في صفحات الفعالية"]),
            ("UNIVERSITIES", "الجامعات", ["خصم الطلاب 25٪ على الاشتراك السنوي", "مقاعد لدفعات كاملة بلوحة للمشرف الأكاديمي", "تقارير تقدّم للطلاب قابلة للتصدير", "مختبرات مرتبطة بـ NCA CCC وPDPL تكمل المقررات"]),
            ("COMPANIES", "الشركات", ["مقاعد للموظفين بـ 80 ر.س للمقعد شهريًا", "لوحة لمسؤول الفريق وتقارير CSV وPDF", "معسكرات خاصة بمحتوى يناسب بيئة الشركة", "فعاليات CTF داخلية لفرق الأمن والتقنية"])],
  # تواصل
  h_con="لنبنِ شراكة", p_con="للأندية والجامعات والشركات والجهات المنظمة للمعسكرات: تواصلوا معنا لتصميم برنامج يناسبكم.",
  links=[("المنصة", "razeen-academy.pages.dev", SITE), ("البريد", "razeenacad@gmail.com", "mailto:razeenacad@gmail.com"), ("إكس", "@razeenaca", "https://x.com/razeenaca")],
  foot="© 2026 أكاديمية رزين", foot2="الأرقام والأسعار بتاريخ نوفمبر 2026",
)
T["en"] = dict(
  dir="ltr", title="Razeen Academy — Portfolio", desc="Razeen Academy portfolio: who we are, our services, plans and discounts, our 12-month plan, and what we offer student clubs, universities and companies.",
  other="/razeen/", other_lbl="العربية", skip="Skip to content", brand="Razeen Academy", brand_sub="PORTFOLIO · 2026",
  nav=[("#about", "About me"), ("#platform", "Platform"), ("#services", "Services"), ("#plans", "Plans"), ("#roadmap", "Plan"), ("#partners", "Partners")],
  visit="Visit platform", badge="Portfolio · November 2026",
  h1='Cloud computing in Arabic,<br><mark>learned by doing</mark>',
  lead="Razeen Academy is a Saudi platform for learning cloud computing and cloud security through hands-on labs and challenges in real environments, mapped to Saudi regulations, from beginner to professional.",
  cta1="Try it free", cta2="Contact us", print="Download PDF",
  facts=[("15", "cloud specializations"), ("3", "providers: AWS, Azure, Google"), ("8", "free labs and challenges published"), ("4", "levels, beginner to professional"), ("2", "languages: Arabic and English")],
  k_about="FILE-01 · FOUNDER", h_about="About the founder",
  name="Razan Aloufi", role="Founder, Razeen Academy · Cloud Computing Specialist",
  dl=[("Specialty", "Cloud Computing Specialist")],
  about_p=[
    "I work across every area of cloud computing, every day: building infrastructure, securing it, and aligning it with Saudi Arabia's Cloud Cybersecurity Controls (NCA CCC) and the Personal Data Protection Law (PDPL).",
    "Most hands-on cloud content is written in English, and many learners study the theory without ever touching a real environment — or connecting it to the regulations that actually apply in Saudi Arabia.",
    "I built Razeen to close that gap: labs you solve yourself, in a language you think in, with every vulnerability tied to the control it breaks.",
  ],
  quote="My goal is for every Razeen learner to graduate having actually done it — not just memorized it.",
  k_plat="FILE-02 · PLATFORM", h_plat="About the platform", p_plat="Razeen is closer to a hands-on challenge platform than a course: you learn by solving scenarios that simulate real incidents at fictional companies.",
  why=[("cloud", "Hands-on in real environments", "You find the flaw yourself on real cloud services. The server verifies every answer, and only what you actually solved counts."),
       ("shield", "Mapped to Saudi regulations", "Every lab links each flaw to the NCA CCC and PDPL control it violates, and shows your mastery of each control with an explanation."),
       ("lang", "Arabic first", "Explanations, questions and hints in Arabic, with technical terms as you'll see them at work — and a full English version of the platform.")],
  journey_h="The learner journey at every level", journey=[("LEARN", "Learn", "Labs that explain a concept and apply it step by step."), ("PRACTICE", "Practice", "Short daily challenges that lock in what you learned."), ("PROVE", "Prove", "CTF challenges, and a certificate when you complete a full track.")],
  specs_h="Fifteen specializations",
  groups=[("Foundations and cloud providers", ["Cloud Fundamentals", "AWS", "Microsoft Azure", "Google Cloud"]),
          ("Engineering and operations", ["Cloud Architecture & Engineering", "DevOps & CI/CD", "Containers & Kubernetes", "Infrastructure as Code", "Cloud Networking", "Databases & Storage", "Monitoring & Operations", "Cost Optimization"]),
          ("Security and data", ["Cloud Security & SOC", "CTF & Security Challenges", "Data & AI Cloud Services"])],
  specs_note="Every specialization is planned on all three providers. Available today: the AWS beginner track; the rest rolls out on the plan below.",
  k_srv="FILE-03 · SERVICES", h_srv="Services", p_srv="Each service shows its real status: “Available now” means it works on the platform today.",
  now="Available now", soon="Coming soon", plan="Planned",
  services=[("lab", "Hands-on labs", "now", "Cloud incident scenarios you solve step by step. Three free AWS labs are live now; intermediate and advanced labs come with a subscription."),
            ("cal", "Daily challenges", "now", "A series of short beginner challenges on AWS, free for every registered learner — a new one each day."),
            ("path", "Tracks and levels", "now", "Four levels (beginner, intermediate, advanced, professional) in each specialization, with a fully free beginner track."),
            ("cert", "Completion certificates", "now", "An English certificate for completing a full track, verifiable by anyone on the platform's verification page."),
            ("trophy", "Leaderboard and CTF events", "now", "A public points leaderboard, plus CTF events with a live board for organizers and bootcamps — such as the Azure Cloud Security Camp CTF with Eager."),
            ("tent", "Bootcamps", "now", "Intensive bootcamps with partner organizers, including custom labs and a final challenge day."),
            ("users", "Team plans", "soon", "Seats for employees or a student cohort, with a manager dashboard and exportable progress reports."),
            ("cloud", "Real-environment sessions", "soon", "An isolated cloud environment per learner, created automatically and removed after the session — no personal cloud account needed.")],
  k_why="FILE-04 · SUBSCRIBER BENEFITS", h_why="What subscribers get", p_why="The beginner level stays completely free, with solutions and hints. A subscription unlocks everything after it:",
  benefits=[("lab", "Intermediate and advanced labs", "Deeper scenarios that simulate real incidents at companies, depending on your plan."),
            ("cloud", "A real cloud environment of your own", "Sessions in an isolated environment (25 a month on Basic, 50 on Professional) — no personal cloud account or credit card needed.", "soon"),
            ("path", "Fresh content all the time", "New labs and challenges every month on AWS, Azure and Google Cloud."),
            ("shield", "Saudi regulations mastery", "Every flaw mapped to NCA CCC and PDPL controls, with your mastery of each control and an explanation."),
            ("cert", "Verifiable completion certificates", "A certificate for every track you complete, verifiable directly by employers."),
            ("trophy", "Leaderboard and public profile", "Your points and achievements on the leaderboard, and a public profile to share with employers."),
            ("flag", "CTF events and bootcamps", "Priority access to Razeen events and bootcamps with partner organizations."),
            ("users", "Student-friendly pricing", "25% student discount on yearly plans, and the founders offer for the first 100 subscribers.")],
  k_plans="FILE-05 · PLANS", h_plans="Plans and pricing", p_plans="Prices in Saudi riyals. Yearly saves up to 29% compared with monthly.",
  th=["Plan", "Price", "Levels", "Real-environment sessions", "Best for"],
  plans=[("Free", "0", "", "Beginner, with solutions and hints", "—", "Anyone starting in cloud"),
         ("Basic", "50", "per month · or 450 per year", "Beginner + Intermediate", "25 per month", "Students and self-learners"),
         ("Professional", "100", "per month · or 850 per year", "Beginner + Intermediate + Advanced", "50 per month", "Practitioners and certification prep"),
         ("Teams", "80", "per seat per month · minimum 10 seats", "Professional levels for every member", "Per plan", "Companies, universities and clubs"),
         ("Bootcamps", "2,500 – 4,000", "per bootcamp", "Custom bootcamp content", "By agreement", "Bootcamp organizers")],
  plans_note="Cancelling renewal keeps access until the end of the paid period. When a subscription ends, the account returns to Free and keeps all progress and certificates. Online payment for subscriptions opens soon.",
  disc_h="Discounts",
  discounts=[("Founders offer", "First 100 subscribers only", "Basic yearly for SAR 270 instead of 450, Professional yearly for SAR 510 instead of 850 (40% off)."),
             ("Student discount", "25% off yearly", "For university students after verifying their university email; valid for one year."),
             ("Partner coupons", "Clubs and events", "Dedicated discount codes for student club members and bootcamp or event participants."),
             ("Discount policy", "Best single discount", "Discounts don't stack; the best one for the learner is applied automatically and calculated on the server only.")],
  k_vis="FILE-06 · VISION", h_vis="Where the platform is heading",
  vis_lead="To make Razeen the leading Arabic platform for hands-on cloud learning — the bridge between what students learn and what the Saudi job market needs.",
  vision=[("cert", "Certification vouchers and discounts", "I will reach out to cloud providers (AWS, Microsoft and Google Cloud) and testing centers to offer vouchers and discounts on their professional certifications for Razeen subscribers — training and exam in one place."),
          ("cloud", "All three providers", "Every one of the fifteen specializations on AWS, Azure and Google Cloud, so learners can compare providers and choose what fits their market."),
          ("path", "New sections such as career paths", "Sections that connect learning to real cloud jobs: a career path for each specialization, with the skills and certifications each role needs."),
          ("users", "Education partnerships", "Ongoing programs with student clubs, universities and companies, including CTF events, bootcamps and team seats.")],
  k_road="FILE-07 · 12-MONTH PLAN", h_road="The 12-month plan", p_road="The plan adapts to what learners and partners need.",
  road=[("Phase 1", "Commercial launch", ["Open paid subscriptions through a Saudi payment gateway", "Activate the founders offer for the first 100", "Run isolated per-learner environments"]),
        ("Phase 2", "More providers", ["Launch the Microsoft Azure track", "First Google Cloud labs", "Launch the student clubs program"]),
        ("Phase 3", "Certifications and companies", ["Reach out to cloud providers for certification vouchers and discounts", "Launch the advanced level", "Activate team plans and the company dashboard", "Bootcamps with training partners"]),
        ("Phase 4", "New sections and levels", ["Add new site sections such as career paths and more", "Launch the professional level", "An open annual Razeen CTF", "An annual impact and statistics report"])],
  k_par="FILE-08 · PARTNERSHIPS", h_par="What we offer clubs, universities and companies",
  partners=[("STUDENT CLUBS", "Student clubs", ["Free CTF event hosting with a live leaderboard", "A dedicated discount code for club members", "Co-hosted hands-on workshops on the platform", "Featured as a partner on event pages"]),
            ("UNIVERSITIES", "Universities", ["25% student discount on yearly plans", "Seats for whole cohorts with an instructor dashboard", "Exportable student progress reports", "Labs mapped to NCA CCC and PDPL that complement courses"]),
            ("COMPANIES", "Companies", ["Employee seats at SAR 80 per seat per month", "A team-manager dashboard with CSV and PDF reports", "Private bootcamps tailored to your environment", "Internal CTF events for security and tech teams"])],
  h_con="Let's build a partnership", p_con="Student clubs, universities, companies and bootcamp organizers: get in touch and we'll design a program around you.",
  links=[("Platform", "razeen-academy.pages.dev", SITE), ("Email", "razeenacad@gmail.com", "mailto:razeenacad@gmail.com"), ("X", "@razeenaca", "https://x.com/razeenaca")],
  foot="© 2026 Razeen Academy", foot2="Figures and prices as of November 2026",
)

def page(lang):
    t = T[lang]; pre = "../" if lang == "en" else ""; a = pre + "assets/"
    site = SITE + ("/en/" if lang == "en" else "/")
    tagcls = {"now": "now", "soon": "soon", "plan": "plan"}
    o = []
    o.append(f'''<!DOCTYPE html>
<html lang="{lang}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t["title"])}</title>
<meta name="description" content="{E(t["desc"])}">
<meta property="og:title" content="{E(t["title"])}"><meta property="og:description" content="{E(t["desc"])}">
<link rel="icon" href="{a}logo-stamp.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{'ar' if lang=='en' else 'en'}" href="https://razan-aloufi.github.io{t["other"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Almarai:wght@400;700&family=IBM+Plex+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="{a}portfolio.css">
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="top"><div class="wrap">
  <a class="brand" href="#top"><img src="{a}logo-stamp.svg" alt="" width="42" height="42"><span>{E(t["brand"])}<small>{t["brand_sub"]}</small></span></a>
  <nav aria-label="{E(t['title'])}">''' + "".join(f'<a href="{h}">{E(l)}</a>' for h, l in (t["nav"][:2] + [("#method", LABS_C[lang]["nav"])] + t["nav"][2:])) + f'''<a class="lang" href="{t["other"]}" lang="{'ar' if lang=='en' else 'en'}">{t["other_lbl"]}</a><a class="solid" href="{site}">{E(t["visit"])}</a></nav>
</div></header>
<main id="main">
<section class="hero" id="top"><div class="wrap">
  <div>
    <span class="badge">{E(t["badge"])}</span>
    <h1>{t["h1"]}</h1>
    <p class="lead">{E(t["lead"])}</p>
    <div class="acts noprint"><a class="cta primary" href="{site}">{E(t["cta1"])}</a><a class="cta" href="#contact">{E(t["cta2"])}</a></div>
  </div>
  <div class="seal"><img src="{a}logo-stamp.svg" alt="{E(t['brand'])}" width="300" height="300"></div>
</div>
<div class="wrap"><div class="facts">''' + "".join(f'<div><b>{n}</b><span>{E(l)}</span></div>' for n, l in t["facts"]) + '</div></div></section>')

    # عنّي
    o.append(f'''<section class="file" id="about"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_about"]}</span><h2>{E(t["h_about"])}</h2></div>
<div class="dossier"><div class="id"><span class="kick">CASE OWNER</span><h3>{E(t["name"])}</h3><p class="role">{E(t["role"])}</p><dl>''' +
      "".join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k, v in t["dl"]) +
      '</dl></div><div class="txt">' + "".join(f'<p>{E(p)}</p>' for p in t["about_p"]) + f'<blockquote>{E(t["quote"])}</blockquote></div></div></div></section>')

    # المنصة
    o.append(f'''<section class="file" id="platform"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_plat"]}</span><h2>{E(t["h_plat"])}</h2><p>{E(t["p_plat"])}</p></div>
<div class="grid g3">''' + "".join(f'<article class="card">{icon(i)}<h3>{E(h)}</h3><p>{E(p)}</p></article>' for i, h, p in t["why"]) + f'''</div>
<h3 style="margin:2.2rem 0 1rem;font-weight:400;font-size:1.3rem">{E(t["journey_h"])}</h3>
<div class="flow">''' + '<span class="arr" aria-hidden="true">→</span>'.join(
        f'<article class="card"><span class="tag code {c}">{k}</span><h3 style="margin-top:.6rem">{E(h)}</h3><p>{E(p)}</p></article>'
        for (k, h, p), c in zip(t["journey"], ["now", "soon", "plan"])) + f'''</div>
<h3 style="margin:2.2rem 0 1rem;font-weight:400;font-size:1.3rem">{E(t["specs_h"])}</h3>
<div class="grid g3 specs">''' + "".join(f'<article class="card"><h3>{E(g)} · {len(s)}</h3><div class="chips">' + "".join(f'<span>{E(x)}</span>' for x in s) + '</div></article>' for g, s in t["groups"]) +
      f'</div><p class="note">{E(t["specs_note"])}</p></div></section>')

    # كيف تعمل المختبرات (labs_section.py)
    o.append(labs_section(lang))

    # الخدمات
    o.append(f'''<section class="file" id="services"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_srv"]}</span><h2>{E(t["h_srv"])}</h2><p>{E(t["p_srv"])}</p></div>
<div class="grid g4">''' + "".join(f'<article class="card">{icon(i)}<h3>{E(h)} <span class="tag {tagcls[s]}">{E(t[s])}</span></h3><p>{E(p)}</p></article>' for i, h, s, p in t["services"]) + '</div></div></section>')

    # مميزات المشتركين
    o.append(f'''<section class="file" id="why"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_why"]}</span><h2>{E(t["h_why"])}</h2><p>{E(t["p_why"])}</p></div>
<div class="grid g4">''' + "".join(f'<article class="card{" lift" if i < 2 else ""}">{icon(b[0])}<h3>{E(b[1])}' + (f' <span class="tag {b[3]}">{E(t[b[3]])}</span>' if len(b) > 3 else '') + f'</h3><p>{E(b[2])}</p></article>' for i, b in enumerate(t["benefits"])) + '</div></div></section>')

    # الباقات
    cur = "SAR" if lang == "en" else "ر.س"
    o.append(f'''<section class="file" id="plans"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_plans"]}</span><h2>{E(t["h_plans"])}</h2><p>{E(t["p_plans"])}</p></div>
<div class="tbl"><table><thead><tr>''' + "".join(f'<th scope="col">{E(h)}</th>' for h in t["th"]) + '</tr></thead><tbody>' +
      "".join(f'<tr><th scope="row">{E(n)}</th><td class="price">{p} {cur}' + (f'<small>{E(s)}</small>' if s else '') + f'</td><td>{E(l)}</td><td>{E(ss)}</td><td>{E(f)}</td></tr>' for n, p, s, l, ss, f in t["plans"]) +
      f'''</tbody></table></div><p class="note">{E(t["plans_note"])}</p>
<h3 style="margin:2.2rem 0 1rem;font-weight:400;font-size:1.3rem">{E(t["disc_h"])}</h3>
<div class="grid g4">''' + "".join(f'<article class="card{" lift" if i == 0 else ""}"><span class="kick">{E(s)}</span><h3>{E(h)}</h3><p>{E(p)}</p></article>' for i, (h, s, p) in enumerate(t["discounts"])) + '</div></div></section>')

    # التوجه
    o.append(f'''<section class="file" id="vision"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_vis"]}</span><h2>{E(t["h_vis"])}</h2><p>{E(t["vis_lead"])}</p></div>
<div class="grid g2">''' + "".join(f'<article class="card{" lift" if i == 0 else ""}">{icon(ic)}<h3>{E(h)}</h3><p>{E(p)}</p></article>' for i, (ic, h, p) in enumerate(t["vision"])) + '</div></div></section>')

    # الخطة
    o.append(f'''<section class="file" id="roadmap"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_road"]}</span><h2>{E(t["h_road"])}</h2><p>{E(t["p_road"])}</p></div>
<ol class="road" style="list-style:none;padding:0;margin:0">''' + "".join(f'<li class="q"><span class="when">{E(w)}</span><h3>{E(h)}</h3><ul>' + "".join(f'<li>{E(x)}</li>' for x in xs) + '</ul></li>' for w, h, xs in t["road"]) + '</ol></div></section>')

    # الشراكات
    o.append(f'''<section class="file partner" id="partners"><div class="wrap">
<div class="sec-h"><span class="kick">{t["k_par"]}</span><h2>{E(t["h_par"])}</h2></div>
<div class="grid g3">''' + "".join(f'<article class="card lift"><span class="for">{k}</span><h3>{E(h)}</h3><ul>' + "".join(f'<li>{E(x)}</li>' for x in xs) + '</ul></article>' for k, h, xs in t["partners"]) + '</div></div></section>')

    # تواصل
    o.append(f'''<section class="file" id="contact"><div class="wrap">
<div class="contact"><div><span class="kick" style="color:var(--peach)">FILE-09 · CONTACT</span><h2>{E(t["h_con"])}</h2><p>{E(t["p_con"])}</p></div>
<div class="links">''' + "".join(f'<a href="{u}"' + ('' if u.startswith("mailto") else ' target="_blank" rel="noopener"') + f'><b>{E(l)}</b><span>{E(v)}</span></a>' for l, v, u in t["links"]) + f'''</div></div></div></section>
</main>
<footer class="wrap"><span>{E(t["foot"])}</span><span>{E(t["foot2"])}</span></footer>
</body></html>
''')
    return "\n".join(o)

(ROOT / "index.html").write_text(page("ar"), encoding="utf-8")
(ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8")
print("built")
