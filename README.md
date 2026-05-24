# 📊 EDA Tool — Exploratory Data Analysis

A Python-based Exploratory Data Analysis tool with two interfaces:
- **Terminal** — interactive menu-driven CLI
- **Streamlit** — web-based UI with file upload support

---

## 📁 Project Structure

```
EDA Project/
│
├── app.py                    # Streamlit web application
├── main.py                    # Entry point — data loading
├── menu.py                    # Terminal menu interface
├── eda_utils.py               # Orchestration layer for terminal flow
├── numeric_information.py     # All numeric column analysis functions
└── categorical_information.py # All categorical column analysis functions
```

---

## ⚙️ How Each File Fits Together

```
main.py  ──────────────────────────────►  data_reading()
   │                                        (loads CSV)
   │
   ├──► menu.py  ──► eda_utils.py  ──► numeric_information.py
   │    (Terminal)                  └──► categorical_information.py
   │
   └──► app.py  ──────────────────► numeric_information.py
        (Streamlit)              └──► categorical_information.py
```

---

## 🚀 Getting Started

### Prerequisites

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn streamlit
```

### Running the Streamlit App

```bash
streamlit run app.py
```

### Running the Terminal Version

```bash
python main.py
```

---

## 🌐 Streamlit App — Features (`app.py`)

### File Upload
- Upload any `.csv` file directly from your desktop via the file uploader
- App halts gracefully until a file is provided

### DataFrame Section
| Feature | Description |
|---|---|
| Shape | Displays total rows and columns |
| Column Information | Shows datatype, non-null count, null count, and null percentage for every column |
| Sample Rows | User selects how many random rows to preview |

### Column Analysis Section — Numeric Columns
| Feature | Description |
|---|---|
| Basic Description | Mean, Median, Std Dev, and full `.describe()` output |
| Outlier Detection | Auto-selects Z-Score method (normal distribution) or IQR method (skewed) |
| Missing Value Analysis | Null count, percentage, and suggested treatment |
| Missing Value Imputation | User chooses Yes/No to trigger imputation |

### Column Analysis Section — Categorical Columns
*(Coming soon — plot functions pending `return fig` fix)*
| Feature | Description |
|---|---|
| Basic Summary | Unique count and mode |
| Value Counts | Full frequency table |
| Missing Value Analysis | Null count, percentage, and suggested treatment |
| Missing Value Imputation | User chooses Yes/No to trigger imputation |

---

## 🖥️ Terminal App — Features (`menu.py`)

```
------------- EDA MENU -------------
1. Basic Information about Data
2. Information about a Particular Column
3. Exit
------------------------------------
```

For numeric columns, further options include:
1. Basic DataFrame Info
2. Describe Column
3. Skew & KDE Plot
4. Outlier Detection
5. Missing Value Calculation
6. Missing Value Imputation

---

## 🔧 Function Reference

### `numeric_information.py`

| Function | Description | Returns |
|---|---|---|
| `Describing_numeric_column(df, col)` | Mean, std dev, describe | `mean, std_dev` |
| `calculate_skew_and_plot_kdeplot(df, col)` | Skew value + KDE plot | `skew_value` |
| `outlier_detection(df, col, skew, mean, std_dev)` | Detects outliers using Z-Score or IQR | `Q1, Q2, Q3, IQR, Lower_Bound, Upper_Bound, new_df` |
| `missing_value_calculation(df, col)` | Null count, percentage, verdict | `null_values, null_pct, message` |
| `whether_to_impute_missing_values(df, col, choice)` | Triggers imputation based on user choice | `status message` |
| `missing_value_treatment(df, col)` | Applies chosen imputation method | Modifies dataframe in place |

### `categorical_information.py`

| Function | Description | Returns |
|---|---|---|
| `counting_information(df, col)` | Unique count, mode, value counts | Prints to console |
| `plot_countplot(df, col)` | Bar chart or pie chart based on cardinality | Prints to console |

---

## 🧠 Outlier Detection Logic

The `outlier_detection()` function automatically picks the right method based on skew:

```
Skew ≤ 1  →  Z-Score Method   →  Lower = mean - 3*std,  Upper = mean + 3*std
Skew > 1  →  IQR Method       →  Lower = Q1 - 1.5*IQR,  Upper = Q3 + 1.5*IQR
```

---

## 🔮 Pending / Coming Soon

- `calculate_skew_and_plot_kdeplot()` — needs `return fig` fix to render in Streamlit
- `plot_countplot()` — needs `return fig` fix to render in Streamlit
- Download button to export cleaned dataframe as CSV

---

## 👤 Author

Built as a learning project to practice EDA, OOP, and Streamlit development.
