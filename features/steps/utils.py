from DishDecoderApp.models import Product_Nutrients

def toggle_down_navbar(context):
    toggler_btn = context.browser.find_by_css('button[class="navbar-toggler"]')
    if toggler_btn:
        toggler_btn.click()

def get_nutritional_value_foreach_nutrition(rec_prod):
        nut_value = {} 
        for rel_rec_prod in rec_prod:
            for rel_prod_nut in Product_Nutrients.objects.filter(id_product=rel_rec_prod.id_product):
                unit = rel_rec_prod.id_product.unit
                value = rel_rec_prod.quantity * (rel_prod_nut.quantity / 100)
                nut_id = rel_prod_nut.id_nutrient.id
                if unit == 'L':
                    value *= 1000
                if nut_id not in nut_value:
                    nut_value[nut_id] = {'value':value, 'nutrient' : rel_prod_nut.id_nutrient}
                else:
                    nut_value[nut_id]['value'] += value
        return [list(total_nut_val.values()) for total_nut_val in nut_value.values()]