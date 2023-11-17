from datetime import datetime, timezone, timedelta

# Valor de época (em segundos)
epoch_value = 1620066626  # Substitua isso pelo seu valor de época

# Criar um objeto datetime a partir do valor de época
dt = datetime.fromtimestamp(epoch_value, tz=timezone.utc)

# Definir o fuso horário para São Paulo
fuso_horario_sao_paulo = timezone(timedelta(hours=-3))  # UTC-3

# Converter para o fuso horário de São Paulo
dt_sao_paulo = dt.astimezone(fuso_horario_sao_paulo)

# Converter para uma string formatada
data_hora_formatada = dt_sao_paulo.strftime("%Y-%m-%d %H:%M:%S %Z")

# Imprimir a data e hora formatada no fuso horário de São Paulo
print("Data e hora em São Paulo:", data_hora_formatada)
