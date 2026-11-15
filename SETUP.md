# הקמת סביבת עבודה (Windows)

כל הפקודות ב־PowerShell, מתוך שורש המאגר (התיקייה שבה נמצא `README.md`).

## 1. לוודא ש־Python 3.14 (גרסת הקורס) מותקן

```powershell
py -3.14 --version
```

אמור להופיע `Python 3.14.x`. אם `py` לא מוכר, נסי `python --version`. אם הגרסה לא 3.14, פני למרצה.

## 2. ליצור סביבה וירטואלית (פעם אחת)

```powershell
py -3.14 -m venv .venv
```

נוצרת תיקייה `.venv`. היא לא נכנסת ל־git (ראי `.gitignore`).

## 3. להפעיל את הסביבה (בכל מסוף חדש)

```powershell
.venv\Scripts\Activate
```

בתחילת השורה במסוף מופיע `(.venv)`. **אם אין `(.venv)` — הסביבה לא מופעלת**, ו־`python` הוא ה־Python הכללי של המחשב.
מסוף חדש ב־VS Code מפעיל את הסביבה לבד, אחרי שבחרת את המפרש (סעיף 7).

## 4. להתקין את החבילות

```powershell
python -m pip install -r requirements-dev.txt
```

## 5. בדיקת תקינות

```powershell
python -m tools.doctor
```

`doctor` בודק: גרסת Python, סביבה וירטואלית, חבילות, UTF-8, SQLite, אזורי זמן. כל בעיה מגיעה עם הוראת תיקון.

## 6. הרצת הבדיקות

```powershell
python -m pytest
```

## 7. VS Code

`Ctrl+Shift+P` ← **Python: Select Interpreter** ← לבחור את המפרש שבתוך `.venv`.
ממפגש 5 הבדיקות מופיעות גם בלשונית **Testing**, ומשם אפשר להריץ אותן בדיבאגר (**Debug Test**).

## למה `python -m pytest` ולא `pytest`?

`python -m ...` מריץ את הכלי עם **אותו** Python שמופיע לפני ה־`-m`. אם הסביבה לא מופעלת, `pytest` לבד עלול לרוץ מהתקנה אחרת במחשב, עם גרסה אחרת וחבילות אחרות. אותו דבר ל־`pip`.

## תקלות נפוצות

| אם קורה... | נסי... |
|---|---|
| `Activate` נחסם ("running scripts is disabled") | פעם אחת: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. או בלי הפעלה, עם נתיב מלא: `.venv\Scripts\python -m pytest` |
| `py` לא מוכר | `python --version`; אם זו גרסת הקורס, השתמשי ב־`python` במקום `py -3.14` |
| `doctor` מדווח גרסה אחרת | למחוק את `.venv` וליצור מחדש עם הגרסה הנכונה |
| עברית מופיעה כ־`???` | להגדיר `PYTHONUTF8=1` (ההוראה המדויקת ב־`doctor`) ולפתוח מסוף חדש |
| המאגר בתוך OneDrive | להעביר ל־`C:\dev\` |
| `pytest` לא מוצא מודול | להריץ משורש המאגר |
| `pip` נתקע | ייתכן סינון רשת במעבדה; לפנות לטכנאי |
