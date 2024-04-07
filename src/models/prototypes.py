class Template:
    def __init__(self,sheet):
        self.sheet=sheet
        
    def constructor(self):
        pass
    
    def __str__(self) -> str:
        return str(self.constructor())


class SheetObject(Template):
    def __init__(self,sheet,fields,data):
       super().__init__(sheet)
       self.fields=fields
       self.data=data
    
    def constructor(self):
        books =list() # liobreria ficticia
        book = dict() # libro 
        for row in self.data: # recorre filas de la tabla
            for i,value in enumerate(row): # recorre columnas de la tabla
                book[f"{self.fields[i].lower()}"]=value # crea datos de un libro
            books.append(book.copy()) # agrega un libro a la libreria
        return books
    
    def __str__(self):
        return super().__str__()        

       
class Sheet(Template):
    def __init__(self,path,num):
        super().__init__(path)
        self.index = num
    
    def constructor(self):
        return {"sheet":f"/{self.sheet}","index":self.index}
    
    def __str__(self):
        return super().__str__()        