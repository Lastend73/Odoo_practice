from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class product_main(models.Model):
    _name = 'product.main'
    _description = "Product Main"
    
    Product_Class = fields.Many2one("product.class", string="Product Class") 
    Product_Line = fields.Many2one("product.line", string="Product Line", domain="[('Product_Class','=',Product_Class)]" )
    Product_Model= fields.Many2one("product.model", string="Product Model", domain="[('Product_Class','=',Product_Class),('Product_Line','=',Product_Line)]" )
    Product_Generation= fields.Many2one("product.generation", string="Product Generation", domain="[('Product_Class','=',Product_Class),('Product_Line','=',Product_Line),('Product_Model','=',Product_Model)]") 
    Product_Nation = fields.Char(string="Product Nation") 
    Note = fields.Text(string="Notes") 
   
    @api.onchange('Product_Class')
    def onchange_Class(self): 
            self.Product_Line =""
            self.Product_Model =""
            self.Product_Generation =""
       
    @api.onchange('Product_Line')
    def onchange_Line(self):
            self.Product_Model =""
            self.Product_Generation =""

    @api.onchange('Product_Model')
    def onchange_Model(self):
            self.Product_Generation =""

    def add_product_class(self):
        return {
                "name":"Add Product Class",
                "type" : "ir.actions.act_window",
                "res_model" : "create.product.class",
                "view_mode" : "form",
                "target" : "new", #popup 하려면 필요한 옵션(?)
                "context" : {
                        'user_data_id' : self.id
                        }
        }
    
    def add_product_line(self):
        return {
                "name":"Add Product Line",
                "type" : "ir.actions.act_window",
                "res_model" : "create.product.line",
                "view_mode" : "form",
                "target" : "new", #popup 하려면 필요한 옵션(?)
                "context" : {
                        "default_Product_Class": self.Product_Class.id,
                        'user_data_id' : self.id
                        }
        }
    
    def add_product_model(self):
        return {
                "name":"Add Product model",
                "type" : "ir.actions.act_window",
                "res_model" : "create.product.model",
                "view_mode" : "form",
                "target" : "new", #popup 하려면 필요한 옵션(?)
                "context" : {
                        "default_Product_Class": self.Product_Class.id,
                        "default_Product_Line": self.Product_Line.id,
                        'user_data_id' : self.id
                        }
        }
    
        
    def add_product_generation(self):
        return {
                "name":"Add Product generation",
                "type" : "ir.actions.act_window",
                "res_model" : "create.product.generation",
                "view_mode" : "form",
                "target" : "new", #popup 하려면 필요한 옵션(?)
                "context" : {
                        "default_Product_Class": self.Product_Class.id,
                        "default_Product_Line": self.Product_Line.id,
                        "default_Product_Model": self.Product_Model.id,
                        'user_data_id' : self.id
                        }
        }
    

