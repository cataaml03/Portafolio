"""
Configuración central del proyecto.

Las credenciales se leen desde el archivo .env (NUNCA subir credenciales a GitHub).
Copien .env.example a .env y completen sus claves.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Rutas del proyecto
RAIZ = Path(__file__).resolve().parents[1]
RUTA_DATOS = RAIZ / "data"
RUTA_DB = RUTA_DATOS / "coyuntura.db"
RUTA_SQL = RAIZ / "sql"

# Cargar credenciales desde .env
load_dotenv(RAIZ / ".env")

# --- Banco Central de Chile ---
# Registro gratuito en: https://si3.bcentral.cl/Siete/es/Siete/API
BCCH_USUARIO = os.getenv("BCCH_USUARIO", "")
BCCH_PASSWORD = os.getenv("BCCH_PASSWORD", "")

# --- FRED (Reserva Federal de St. Louis) ---
# API key gratuita en: https://fred.stlouisfed.org/docs/api/api_key.html
FRED_API_KEY = os.getenv("FRED_API_KEY", "")

# ============================================================
# CATÁLOGO DE SERIES DEL PROYECTO
# Cada equipo debe editar este catálogo con sus propias series.
# Los códigos del BCCh se buscan en https://si3.bcentral.cl/siete
# (el código aparece en la ficha de cada serie).
# ============================================================

# Series del Banco Central de Chile
SERIES_BCCH = [
    # (codigo, nombre, frecuencia, unidad, id_tema)
    # El tipo de cambio puede influir en los precios de los productos importados.
    ("F073.TCO.PRE.Z.D", "Tipo de cambio observado (CLP/USD)", "D", "CLP/USD", 5),
    # La TPM permite estudiar la respuesta de la política monetaria frente a la inflación.
    ("F022.TPM.TIN.D001.NO.Z.D", "Tasa de Política Monetaria (TPM)", "D", "% anual", 4),
    # Permite observar los cambios mensuales de los precios.
    ("F074.IPC.VAR.Z.Z.C.M", "IPC, variación mensual", "M", "var. % mensual", 2),
    # El Imacec permite observar cómo evoluciona la actividad económica.
    ("F032.IMC.IND.Z.Z.EP18.Z.Z.0.M", "Imacec (índice)", "M", "índice 2018=100", 1),
    # Es nuestra variable principal para estudiar la inflación en Chile.
    ("F074.IPC.V12.Z.EP23.C.M", "Inflación IPC total interanual", "M", "var. % anual", 2),
    # Permite estudiar los precios de bienes más expuestos al comercio internacional.
    ("F074.IPCT.IND.Z.EP23.Z.M", "IPC transables (índice empalmado)", "M", "índice 2023=100", 2),
    # Permite estudiar los precios de bienes y servicios menos expuestos al comercio internacional.
    ("F074.IPCN.IND.Z.EP23.Z.M", "IPC no transables (índice empalmado)", "M", "índice 2023=100", 2),
    # Ayuda a observar la inflación sin los efectos directos de alimentos y energía.
    ("F074.IPCSAE.IND.Z.EP23.Z.M", "IPC sin alimentos y energía (SAE)", "M", "índice 2023=100", 2),
    # Permite incorporar la situación del mercado laboral al análisis.
    ("F049.DES.TAS.HIST.10.M", "Tasa de desempleo nacional", "M", "%", 3),
    # El petróleo puede influir en los costos de transporte y producción.
    ("F019.PPB.PRE.41AB.M", "Precio internacional del petróleo Brent", "M", "USD/barril", 6),
    ]

# Series de FRED
SERIES_FRED = [
    # (codigo, nombre, frecuencia, unidad, id_tema)
    # Permite conocer el contexto inflacionario de Estados Unidos.
    ("CPIAUCSL", "IPC Estados Unidos (índice)", "M", "índice", 6),
    # Permite considerar la política monetaria de Estados Unidos y su posible influencia externa.
    ("FEDFUNDS", "Tasa Fed Funds (EE.UU.)", "M", "% anual", 6),
    ]