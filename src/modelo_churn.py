"""
TelcoGuard AI - Modelo Predictivo de Fuga de Clientes (Churn)
Responsables: Camila Torres (Ingesta/Ética), Valentina Ruiz (EDA), Lucas Gavazzi (Modelado)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    recall_score,
    precision_score,
    f1_score,
    roc_auc_score,
)


def cargar_y_limpiar_datos(ruta_csv: str) -> pd.DataFrame:
    df = pd.read_csv(ruta_csv)

    # Conversión de TotalCharges a numérico y eliminación de registros nulos (11 filas)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna(subset=["TotalCharges"]).copy()

    # Variable objetivo binaria
    df["Churn_bin"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df


def analizar_patrones_fuga(df: pd.DataFrame) -> None:
    print("=== ANÁLISIS EXPLORATORIO (EDA) ===")
    print(f"Total de clientes válidos: {len(df)}")
    print(f"Tasa global de churn: {df['Churn_bin'].mean() * 100:.2f}%\n")

    print("Tasa de churn por tipo de contrato:")
    print((df.groupby("Contract")["Churn_bin"].mean() * 100).round(2))

    total_bajas = df["Churn_bin"].sum()
    bajas_m2m = df[df["Contract"] == "Month-to-month"]["Churn_bin"].sum()
    print(f"\nConcentración de bajas en contrato Month-to-month: {bajas_m2m / total_bajas * 100:.2f}%\n")


def entrenar_y_evaluar(df: pd.DataFrame) -> None:
    # Marco Ético: exclusión de identificador (PII) y variables demográficas sensibles
    cols_excluir = [
        "customerID",
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "Churn",
        "Churn_bin",
    ]
    X = df.drop(columns=cols_excluir)
    y = df["Churn_bin"]

    # Codificación de variables categóricas
    X_encoded = pd.get_dummies(X, drop_first=True)

    # División entrenamiento / prueba estratificada
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42, stratify=y
    )

    # Random Forest con balanceo de clases para priorizar Recall
    modelo = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        min_samples_leaf=10,
        class_weight="balanced",
        random_state=42,
    )
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    y_prob = modelo.predict_proba(X_test)[:, 1]

    print("=== MÉTRICAS DEL MODELO (RANDOM FOREST) ===")
    print(f"Recall:    {recall_score(y_test, y_pred) * 100:.2f}%")
    print(f"Precision: {precision_score(y_test, y_pred) * 100:.2f}%")
    print(f"F1-Score:  {f1_score(y_test, y_pred) * 100:.2f}%")
    print(f"ROC-AUC:   {roc_auc_score(y_test, y_prob) * 100:.2f}%\n")
    print("Matriz de Confusión:")
    print(confusion_matrix(y_test, y_pred))
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred, target_names=["No Fuga", "Fuga"]))

    # Importancia de variables (Explicabilidad)
    importancias = pd.Series(modelo.feature_importances_, index=X_encoded.columns)
    print("Top 5 variables más influyentes:")
    print((importancias.sort_values(ascending=False).head(5) * 100).round(2))


if __name__ == "__main__":
    df_clientes = cargar_y_limpiar_datos("data/telco_Customer_Churn.csv")
    analizar_patrones_fuga(df_clientes)
    entrenar_y_evaluar(df_clientes)
