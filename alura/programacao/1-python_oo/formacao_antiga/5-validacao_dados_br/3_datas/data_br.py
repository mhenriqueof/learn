from datetime import datetime, timedelta

class Data:
    
    def __init__(self):
        
        self.reg_momment = datetime.today()
        

    def __str__(self):
        
        return self.formatted_date()

    def reg_month(self):
        
        months = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        
        month_year = (self.reg_momment.month - 1)
        
        return months[month_year]
    
    def reg_week(self):
        
        week = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        
        day_week = self.reg_momment.weekday()
        
        return week[day_week]
    
    def formatted_date(self):
        
        return self.reg_momment.strftime('%d/%m/%Y - %H:%M')
    
    def time_register(self):
        
        return datetime.today() + timedelta(days = 15, minutes = 23, hours = 21, seconds = 53) - self.reg_momment
    