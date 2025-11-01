class BadgePrinter:
    def __init__(self):
        self.first_name = None
        self.last_name = None

    def format_name(self,new_first_name,new_last_name):
        clean_first_name=new_first_name.strip()
        clean_last_name=new_last_name.strip()
        if not clean_first_name:
            return "First name cannot be empty."
        elif not clean_last_name:
            return "Last name cannot be empty." 
        elif not clean_first_name.replace(' ','').isalpha():
            return "Invalid first name."
        elif not clean_last_name.replace(' ','').isalpha():
            return "Invalid last name."
        self.first_name= clean_first_name.title()
        self.last_name= clean_last_name.upper()
        return f"{self.last_name},{self.first_name}"
    
    def print_badge(self,name):
        
        first_line  ="*****The Conference******"
        last_line  ="*************************"
        return f"{first_line}\nName: {name}\n{last_line}"
        