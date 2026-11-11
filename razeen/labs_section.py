"""قسم «كيف تعمل المختبرات» في ملف الأعمال: المنهجية والمستويات، أنواع البيئات الثلاثة، ودورة حياة المختبر المعزول.
الحالات: av = متاح حاليًا، dev = قيد التطوير، pl = مخطط مستقبلًا. لا تعرضي شي «متاح» إلا إذا يشتغل فعلًا على المنصة."""
import html
E = html.escape

C = {}
C["ar"] = dict(
  nav="طريقة العمل",
  st={"av": "متاح حاليًا", "dev": "قيد التطوير", "pl": "مخطط مستقبلًا"},
  kick="FILE-02.1 · HOW IT WORKS", h="كيف تعمل المختبرات في رزين", p="منهجية واحدة تتكرر في كل مستوى، وثلاثة أنواع من البيئات حسب ما يحتاجه كل مختبر.",
  legend="دليل الحالة",
  # المنهجية
  m_h="منهجية التدريب والمستويات", m_frame="في كل مستوى", m_avail="المتاح الآن:",
  phases=[("LEARN", "تعلّم", "يتعلّم من خلال المختبرات", "LAB-01 · LAB-02 · LAB-03", "mint"),
          ("PRACTICE", "تدرّب", "يطبّق ما تعلّمه في التحديات الموجّهة", "DAY-01 · DAY-02 · DAY-03 · DAY-04", "lemon"),
          ("PROVE", "أثبت مهارتك", "يثبت مهاراته في تحديات CTF", "DAY-05", "rose")],
  then=["ثم طبّق", "ثم أثبت"], repeat="تتكرر المراحل الثلاث في كل مستوى بمحتوى أعمق وأصعب",
  next="بعد إكماله", passes="يمر بالمراحل الثلاث",
  levels=[("1", "مبتدئ", "Beginner", "مجاني", "av", "LAB-01..03 · DAY-01..05"),
          ("2", "متوسط", "Intermediate", "الأساسية", "dev", "مختبرات أعمق وبيئات حقيقية"),
          ("3", "متقدم", "Advanced", "الاحترافية", "pl", "سيناريوهات متعددة الخدمات"),
          ("4", "احترافي", "Professional", "يُحدد لاحقًا", "pl", "حوادث كاملة على مستوى المنظمة")],
  # أنواع البيئات
  e_h="أنواع بيئات المختبرات", e_root="بيئات مختبرات رزين", e_root_p="كل مختبر يُبنى على النوع المناسب لهدفه وتكلفته",
  steps_l="كيف يعمل", props_l="الخصائص", ex_l="في رزين اليوم",
  envs=[
    dict(k="SIMULATED", n="بيئات المحاكاة", en="Simulated Labs", st="av", ico="sim",
         d="تعمل داخل متصفح رزين على سيناريوهات وملفات وإعدادات بصيغتها الحقيقية.",
         steps=["يبدأ المختبر من المتصفح", "يقرأ ويعدّل ملفات synthetic (سياسة IAM، سجل CloudTrail، Terraform)", "يرسل الحل", "الخادم يتحقق من الإجابة", "يُحفظ التقدّم والإنجاز"],
         props=["بدون موارد سحابية لكل متدرب", "تحقق من جهة الخادم", "تكلفة تشغيل شبه صفرية"],
         ex="LAB-02 · LAB-03 · التحديات الخمسة"),
    dict(k="SHARED REAL", n="بيئات حقيقية مشتركة", en="Shared Real Labs", st="av", ico="shared",
         d="مورد حقيقي واحد لدى مزود السحابة، يستخدمه كل المتدربين ضمن صلاحيات محددة.",
         steps=["يثبّت أداة المزود (مثل AWS CLI) على جهازه", "يتصل بالمورد الحقيقي في حساب الأكاديمية", "ينفّذ أوامر حقيقية", "يدخل ما وجده في رزين", "الخادم يتحقق ويحفظ النتيجة"],
         props=["قراءة فقط: سياسة المورد لا تسمح بأي تعديل أو حذف", "بيانات synthetic بدون أي بيانات حقيقية", "تنبيه ميزانية على حساب الأكاديمية"],
         ex="LAB-01: حاوية Amazon S3 مشتركة للقراءة فقط"),
    dict(k="ISOLATED REAL", n="بيئات حقيقية معزولة", en="Isolated Real Labs", st="dev", ico="iso",
         d="بيئة سحابية مستقلة لكل متدرب، تُنشأ عند البدء وتُحذف بعد الانتهاء.",
         steps=["يبدأ المختبر، ويتحقق النظام من الاشتراك والجلسات", "محرك المختبرات ينشئ الموارد لدى المزود", "يحصل على صلاحية دخول مؤقتة لبيئته", "ينفّذ أوامر وتجارب حقيقية", "تُحفظ النتيجة، ثم تُحذف الموارد"],
         props=["عزل كامل بين المتدربين", "مدة جلسة محددة وإغلاق تلقائي", "صلاحية التعديل داخل بيئته فقط"],
         ex="المبني الآن: التحقق من الباقة وحد الجلسات. المحرك نفسه قيد التطوير"),
  ],
  # دورة الحياة
  l_h="دورة حياة المختبر الحقيقي المعزول", l_p="التصميم المعتمد للمحرك. كل خطوة موضّح بجانبها المكوّن المسؤول عنها وحالتها الحالية.",
  life=[("دخول الطالب", "Access Control", "av"), ("اختيار المختبر", "Access Control", "av"), ("التحقق من الاشتراك والجلسات", "Session Manager", "av"),
        ("طلب إنشاء البيئة", "Lab Engine", "dev"), ("محرك المختبرات", "Lab Engine", "dev"), ("الاتصال بمزود السحابة", "Cloud Connector", "dev"),
        ("إنشاء الموارد المستقلة", "Environment Manager", "dev"), ("إتاحة المختبر للطالب", "Access Control", "dev"), ("التطبيق العملي", "Session Manager", "dev"),
        ("إنهاء المختبر", "Lab Validator", "dev"), ("حفظ الإنجاز", "Lab Validator", "av"), ("حذف الموارد المؤقتة", "Cleanup Manager", "dev"), ("انتهاء الجلسة", "Session Manager", "dev")],
  comp_h="المكوّنات التقنية",
  comps=[("Lab Engine", "يستقبل طلب البيئة وينسّق بقية المكوّنات من البداية إلى الحذف.", "dev"),
         ("Cloud Connector", "يتصل بحسابات الأكاديمية لدى AWS وAzure وGoogle Cloud بصلاحيات محدودة.", "dev"),
         ("Environment Manager", "ينشئ موارد المختبر من قالب جاهز ويتابع حالتها.", "dev"),
         ("Session Manager", "يحسب الجلسات الشهرية حسب الباقة، ويتابع وقت الجلسة.", "dev"),
         ("Access Control", "يتحقق من الحساب والباقة، ويمنح صلاحية دخول مؤقتة للبيئة فقط.", "dev"),
         ("Lab Validator", "يتحقق من حل المتدرب في الخادم ويحفظ التقدّم والإنجاز.", "av"),
         ("Cleanup Manager", "يحذف كل الموارد المؤقتة بعد الإنهاء أو انتهاء الوقت.", "dev")],
  comp_note="Lab Validator يعمل اليوم في كل المختبرات والتحديات. التحقق من الباقة وحد الجلسات مبني ضمن Access Control وSession Manager، وبقية المكوّنات قيد التطوير.",
  auto_h="الإغلاق التلقائي", auto=[("انتهاء الوقت", "تنتهي مدة الجلسة (تُضبط من الإدارة، افتراضيًا 60 دقيقة)"), ("انقطاع الجلسة", "إذا انقطع المتدرب، تُحفظ بيئته مدة قصيرة حسب سياسة التشغيل"), ("الحذف", "Cleanup Manager يحذف الموارد ويُغلق الجلسة"), ("الحفظ", "يبقى تقدّم المتدرب وإنجازاته محفوظة دائمًا")],
)
C["en"] = dict(
  nav="How it works",
  st={"av": "Available", "dev": "In Development", "pl": "Planned"},
  kick="FILE-02.1 · HOW IT WORKS", h="How Razeen labs work", p="One methodology repeated at every level, and three kinds of environment depending on what each lab needs.",
  legend="Status key",
  m_h="Training methodology and levels", m_frame="At every level", m_avail="Available now:",
  phases=[("LEARN", "Learn", "Learns through labs", "LAB-01 · LAB-02 · LAB-03", "mint"),
          ("PRACTICE", "Practice", "Applies it in guided challenges", "DAY-01 · DAY-02 · DAY-03 · DAY-04", "lemon"),
          ("PROVE", "Prove", "Proves skills in CTF challenges", "DAY-05", "rose")],
  then=["then apply", "then prove"], repeat="The three stages repeat at every level, deeper and harder each time",
  next="after completing", passes="Goes through all three stages",
  levels=[("1", "Beginner", "مبتدئ", "Free", "av", "LAB-01..03 · DAY-01..05"),
          ("2", "Intermediate", "متوسط", "Basic", "dev", "Deeper labs and real environments"),
          ("3", "Advanced", "متقدم", "Professional", "pl", "Multi-service scenarios"),
          ("4", "Professional", "احترافي", "To be set", "pl", "Full organization-wide incidents")],
  e_h="Lab environment types", e_root="Razeen lab environments", e_root_p="Each lab is built on the type that fits its goal and cost",
  steps_l="How it works", props_l="Properties", ex_l="In Razeen today",
  envs=[
    dict(k="SIMULATED", n="Simulated Labs", en="بيئات المحاكاة", st="av", ico="sim",
         d="Run inside the Razeen browser on scenarios, files and settings in their real formats.",
         steps=["Starts the lab in the browser", "Reads and edits synthetic files (IAM policy, CloudTrail log, Terraform)", "Submits the fix", "The server verifies the answer", "Progress and achievements are saved"],
         props=["No cloud resources per learner", "Server-side verification", "Near-zero running cost"],
         ex="LAB-02 · LAB-03 · the five challenges"),
    dict(k="SHARED REAL", n="Shared Real Labs", en="بيئات حقيقية مشتركة", st="av", ico="shared",
         d="One real resource at the cloud provider, used by every learner within set permissions.",
         steps=["Installs the provider's tool (e.g. AWS CLI) locally", "Connects to the real resource in the academy account", "Runs real commands", "Enters findings in Razeen", "The server verifies and saves the result"],
         props=["Read-only: the resource policy allows no edits or deletes", "Synthetic data, never real data", "Budget alert on the academy account"],
         ex="LAB-01: a shared, read-only Amazon S3 bucket"),
    dict(k="ISOLATED REAL", n="Isolated Real Labs", en="بيئات حقيقية معزولة", st="dev", ico="iso",
         d="A separate cloud environment per learner, created at start and deleted at the end.",
         steps=["Starts the lab; the system checks plan and sessions", "The lab engine creates resources at the provider", "Gets temporary access to their environment", "Runs real commands and experiments", "Result saved, then resources deleted"],
         props=["Full isolation between learners", "Fixed session length and auto-shutdown", "Write access inside their own environment only"],
         ex="Built now: plan and session-quota checks. The engine itself is in development"),
  ],
  l_h="Isolated real lab lifecycle", l_p="The engine's agreed design. Each step shows the component responsible and its current status.",
  life=[("Learner signs in", "Access Control", "av"), ("Chooses a lab", "Access Control", "av"), ("Plan and session check", "Session Manager", "av"),
        ("Environment requested", "Lab Engine", "dev"), ("Lab engine", "Lab Engine", "dev"), ("Connect to cloud provider", "Cloud Connector", "dev"),
        ("Create isolated resources", "Environment Manager", "dev"), ("Lab opened to learner", "Access Control", "dev"), ("Hands-on practice", "Session Manager", "dev"),
        ("Lab finished", "Lab Validator", "dev"), ("Achievement saved", "Lab Validator", "av"), ("Temporary resources deleted", "Cleanup Manager", "dev"), ("Session ends", "Session Manager", "dev")],
  comp_h="Technical components",
  comps=[("Lab Engine", "Receives the environment request and orchestrates every other component, from start to deletion.", "dev"),
         ("Cloud Connector", "Connects to the academy's AWS, Azure and Google Cloud accounts with limited permissions.", "dev"),
         ("Environment Manager", "Creates lab resources from a ready template and tracks their state.", "dev"),
         ("Session Manager", "Counts monthly sessions per plan and tracks session time.", "dev"),
         ("Access Control", "Checks account and plan, and grants temporary access to the environment only.", "dev"),
         ("Lab Validator", "Verifies the learner's solution on the server and saves progress and achievements.", "av"),
         ("Cleanup Manager", "Deletes every temporary resource after finishing or when time runs out.", "dev")],
  comp_note="Lab Validator runs today in every lab and challenge. Plan and session-quota checks are built within Access Control and Session Manager; the other components are in development.",
  auto_h="Auto-shutdown", auto=[("Time runs out", "The session length ends (set by admins, 60 minutes by default)"), ("Session drops", "If the learner disconnects, the environment is kept briefly per the operating policy"), ("Deletion", "Cleanup Manager deletes resources and closes the session"), ("Saved", "The learner's progress and achievements are always kept")],
)

ICO = {
  "sim": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M7 21h10M9 12l-2 2 2 2M15 12l2 2-2 2"/>',
  "shared": '<path d="M7 17a4 4 0 0 1-.6-8A5.5 5.5 0 0 1 17 7.5 4.5 4.5 0 0 1 17 17z"/><circle cx="6" cy="21" r="1.3"/><circle cx="12" cy="21" r="1.3"/><circle cx="18" cy="21" r="1.3"/><path d="M12 17v2.7M6 19.7 9 17M18 19.7 15 17"/>',
  "iso": '<rect x="2.5" y="10" width="8" height="8" rx="1.5"/><rect x="13.5" y="10" width="8" height="8" rx="1.5"/><path d="M6.5 10V6h11v4M12 3v3"/>',
}
def ico(k): return f'<span class="lx-ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICO[k]}</svg></span>'
def st(c, k): return f'<span class="lx-st {k}">{E(c["st"][k])}</span>'
ARROW = '<span class="lx-arr" aria-hidden="true"><svg viewBox="0 0 40 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 8h34M30 3l6 5-6 5"/></svg></span>'

def section(lang):
    c = C[lang]; o = []
    o.append(f'<section class="file lx" id="method" aria-labelledby="lx-h"><div class="wrap">')
    o.append(f'<div class="sec-h"><span class="kick">{c["kick"]}</span><h2 id="lx-h">{E(c["h"])}</h2><p>{E(c["p"])}</p></div>')
    o.append(f'<div class="lx-legend" role="note"><b>{E(c["legend"])}</b>' + "".join(st(c, k) for k in ("av", "dev", "pl")) + '</div>')

    # ---- 1) المنهجية والمستويات
    o.append(f'<h3 class="lx-h3"><span class="lx-num">A</span>{E(c["m_h"])}</h3>')
    o.append(f'<div class="lx-cycle"><span class="lx-frame-l">{E(c["m_frame"])}</span><ol class="lx-phases">')
    for i, (code, name, desc, avail, col) in enumerate(c["phases"]):
        if i: o.append(f'<li class="lx-link" aria-hidden="true"><small>{E(c["then"][i-1])}</small>{ARROW}</li>')
        o.append(f'<li class="lx-phase {col}"><span class="lx-code">{code}</span><b>{E(name)}</b><p>{E(desc)}</p><span class="lx-avail">{E(c["m_avail"])} <span class="mono">{avail}</span></span></li>')
    o.append(f'</ol><p class="lx-repeat"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 12a8 8 0 0 1 14-5.3M20 4v4h-4M20 12a8 8 0 0 1-14 5.3M4 20v-4h4"/></svg>{E(c["repeat"])}</p></div>')
    o.append(f'<div class="lx-passes" aria-hidden="true">↓ {E(c["passes"])} ↓</div>')
    o.append('<ol class="lx-levels">')
    for i, (n, a, b, plan, s, what) in enumerate(c["levels"]):
        o.append(f'<li class="lx-level s{s} d{i+1}"><span class="lx-ln">{n}</span><b>{E(a)}</b><span class="lx-alt">{E(b)}</span><span class="lx-plan">{E(plan)}</span>{st(c, s)}<small>{E(what)}</small><span class="lx-depth" aria-hidden="true"><i></i><i></i><i></i></span></li>')
        if i < 3: o.append(f'<li class="lx-next" aria-hidden="true">{ARROW}<small>{E(c["next"])}</small></li>')
    o.append('</ol>')

    # ---- 2) أنواع البيئات: خريطة مفاهيم
    o.append(f'<h3 class="lx-h3"><span class="lx-num">B</span>{E(c["e_h"])}</h3>')
    o.append(f'<div class="lx-map"><div class="lx-root"><b>{E(c["e_root"])}</b><small>{E(c["e_root_p"])}</small></div><div class="lx-branches" aria-hidden="true"><i></i><i></i><i></i></div><div class="lx-envs">')
    for e in c["envs"]:
        o.append(f'<article class="lx-env s{e["st"]}"><header>{ico(e["ico"])}<div><span class="lx-code">{e["k"]}</span><h4>{E(e["n"])}</h4><span class="lx-alt">{E(e["en"])}</span></div>{st(c, e["st"])}</header><p class="lx-d">{E(e["d"])}</p>')
        o.append(f'<span class="lx-lbl">{E(c["steps_l"])}</span><ol class="lx-flow">' + "".join(f'<li>{E(x)}</li>' for x in e["steps"]) + '</ol>')
        o.append(f'<span class="lx-lbl">{E(c["props_l"])}</span><ul class="lx-props">' + "".join(f'<li>{E(x)}</li>' for x in e["props"]) + '</ul>')
        o.append(f'<p class="lx-ex"><span>{E(c["ex_l"])}</span>{E(e["ex"])}</p></article>')
    o.append('</div></div>')

    # ---- 3) دورة حياة المختبر المعزول
    o.append(f'<h3 class="lx-h3"><span class="lx-num">C</span>{E(c["l_h"])} {st(c, "dev")}</h3><p class="lx-sub">{E(c["l_p"])}</p>')
    o.append('<ol class="lx-life">')
    for i, (name, comp, s) in enumerate(c["life"], 1):
        o.append(f'<li class="s{s}"><span class="lx-n mono">{i:02d}</span><b>{E(name)}</b><span class="lx-comp mono">{comp}</span>{st(c, s)}</li>')
    o.append('</ol>')
    o.append(f'<div class="lx-bottom"><div><h4 class="lx-h4">{E(c["comp_h"])}</h4><ul class="lx-comps">')
    for name, d, s in c["comps"]:
        o.append(f'<li class="s{s}"><span class="lx-comp mono">{name}</span>{st(c, s)}<p>{E(d)}</p></li>')
    o.append(f'</ul><p class="note">{E(c["comp_note"])}</p></div>')
    o.append(f'<div class="lx-auto"><h4 class="lx-h4">{E(c["auto_h"])} {st(c, "dev")}</h4><ol>' + "".join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in c["auto"]) + '</ol></div></div>')
    o.append('</div></section>')
    return "".join(o)
