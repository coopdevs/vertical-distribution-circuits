from openerp import models, fields, api

class DeliveryRoundWizard(models.TransientModel):
    
    _name="delivery.round.wizard"
    
    time_frame_id = fields.Many2one('time.frame', string="Time Frame", domaine=[('state','=', 'open')], required=True)
    
    def compute_delivery_round(self):
        time_frame = self.time_frame_id
        pickings = self.env['stock.picking'].search([('time_frame_id','=',time_frame.id)])
        #chercher un delivery round existant pour ce time frame
        
        #chercher dans les lignes du delivery round le picking wave correspondant � l'adress
        
        #si non existant le cr�er avec le time_frame_id et l'adresse recherch�
        
        #ajoutez un nouvelle ligne au deliver round avec le picking wave cr��
        
        #y ajouter les picking non assign�s existant 
        
        self.env['stock.picking.wave'].search([('time_frame_id','=',time_frame.id)])
        return True