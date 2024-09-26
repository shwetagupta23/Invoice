# Copyright (c) 2024, SHWETA and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class invoice(Document):
    def validate(self):
        total_amount = 0
        Disc = self.discount or 0

        if not self.items:
            frappe.throw("Please provide the item details!")

        for items in self.items:
            item_total = items.quantity * items.price


            total_amount += item_total

        discount = (Disc / 100) * total_amount
        self.total_amount = total_amount - discount
        self.payable_amount = total_amount - discount