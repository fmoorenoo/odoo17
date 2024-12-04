# -*- coding: utf-8 -*-
import json

from urllib3 import request

from odoo import http


class ListaTareas(http.Controller):
    @http.route('/lista_tareas/lista_tareas', auth='public')
    def index(self, **kw):
        return "Hola"

    @http.route('/lista_tareas/lista_tareas/objects/<model("lista_tareas.lista_tareas"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('lista_tareas.object', {
            'object': obj
        })


    @http.route('/lista_tareas/lista_tareas/objects', auth='public', type='http', methods=['GET'], csrf=False)
    def listado_tareas(self, **kw):
        tareas = request.env['lista_tareas.lista_tareas'].search([])

        tareas_list = []
        for tarea in tareas:
            tareas_list.append({
                'id': tarea.id,
                'tarea': tarea.tarea,
                'prioridad': tarea.prioridad,
                'urgente': tarea.urgente,
                'realizada': tarea.realizada,
            })
        return request.make_response(
            json.dumps(tareas_list),
            headers={'object': 'application/json'}
        )



