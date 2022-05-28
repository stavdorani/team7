Team7

אתר למציאת טרמפים - האתר והאפליקציה שלנו  - Say what? Say ride הינה פלטפורמה למציאת טרמפים בישראל המשמשת עזרה לסטודנטים מבן גוריון המחפשים טרמפ הביתה מבאר שבע. שירותו המרכזי הינו מציאת טרמפים זולים, נוחים ומהירים המותאמים ל"ספונטניות" הסטודנטים הן מבחינת זמני יציאה והגעה והן מבחינת מחירים, ולצד זאת יצירת דפי HTML נוספים:
1.	"Welcome page" - עמוד הבית בו המשתמש יוכל להכנס לחשבון קיים אם כבר נרשם או להרשם כמשתמש חדש.
2.	"Choose service" – בעמוד זה המשתמש יבחר בשירות בו הוא מעוניין: הצעת או חיפוש טרמפ.
3.	"Create ride" - עמוד אשר בו ניתן ליצור טרמפ חדש תוך מילוי הפרטים.
4.	"Find a ride" - עמוד בו המשתמש יוכל לחפש טרמפ לפי הפרטים והפילטרים שיכניס.
5.	"your ride in the system" - עמוד בו המשתמש מקבל אישור שהטרמפ שיצר נוצר בהצלחה.
6.	"Choose ride" - עמוד בו המשתמש יוכל לראות את כל הטרמפים שרלוונטים לחיפוש שלו.
7.	"Edit your ride" – בעמוד זה יוכל המשתמש לערוך את פרטי הטרמפ שיצר.
8.	"Ride history" – בעמוד זה המשתמש יוכל לדרג נהגים שנסע איתם.
9.	Reset password"" – בעמוד זה יוכל המשתמש לאפס את הסיסמא.
10.	Sign in page"" – בעמוד זה יוכל משתמש חדש להרשם במידה והוא לא רשום במערכת.

בכלל העמודים ישנו Navigation Bar אשר מקשר בין העמודים ובאמצעותו ניתן להגיע מדף אחד לשני. 
1.	עיצוב העמודים – באמצעות קובץ CSS אחד אשר משמש לכלל העמודים. בכל עמוד, האלמנטים מותאמים לגודל מסך המשתמש, הן כאפליקציה והן כאתר הנעשה באמצעות grid.
2.	בעיצוב העמודים שילבנו אנימציות לשיפור חווית המשתמש.
3.	עמודים הדורשים קלט מהמשתמש - כתובת מייל- חיוב המשתמש להכניס כתובת מייל תקינה מכילה שטרודל. מספר טלפון- מכיל 10 ספרות בדיוק שיכולות לנוע בטווח 0-9. תאריך טרמפ- ניתן לבחור תאריך רק מהיום והלאה, לא ניתן לבחור תאריך שעבר. סיסמא- סיסמא תקינה חייבת להכיל בין 6-8 תווים.
4.	קיימת אפשרות להציג סיסמא אם המשתמש יבחר בכך ע"י check box. 
5.	מימוש פונקציונאליות של השירות בצד לקוח - המשתמש חייב למלא את כל השדות כראוי. במידה והשדה לא עומד בדרישה קופצת הודעה "שדה זה חובה", כך נוכל להבטיח שהשדות ימולאו באופן תקין ורק לאחר מכן המשתמש יוכל להמשיך הלאה
6.	.
הנחות:
1.	האתר לא מחובר לDB ולכן נתונים יתאפסו ברענון האתר.
2.	בדף ההרשמה "Sign in page" על המשתמש למלא את השדות כראוי על מנת ליצור משתמש חדש ולהיכנס למערכת.
3.	רק לאחר שהטרמפ מופיע ברשימת הטרמפים בעמוד "choose service", המשתמש יכול לגשת ולבצע עריכה לטרמפ שהציע.
