## Setup Python Environment - Terminal
cd project_submission
python -m venv .venv

# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate

pip install streamlit
pip install -r requirements.txt
pip install babel matplotlib seaborn

## Run Streamlit App
streamlit run dashboard.py
