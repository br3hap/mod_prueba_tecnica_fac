/** @odoo-module **/
console.log("button_open_wizard.js cargado");

// import { registry } from "@web/core/registry";
// import { rpc } from "@web/core/network/rpc";
// import { patch } from "@web/core/utils/patch";

// function patchFormRenderer() {
//     const FormRenderer = registry.category("views").get("form");

//     patch(FormRenderer.prototype, "mod_prueba_tecnica_fac.ButtonOpenWizard", {
//         mounted() {
//             this._super(...arguments);
//             console.log("PatchFormRenderer mounted ejecutado");
//             this.el.querySelectorAll(".o_open_wizard_rpc_button").forEach((btn) => {
//                 btn.addEventListener("click", async (ev) => {
//                     ev.preventDefault();
//                     const recordId = this.props.record.id;
//                     const action = await rpc.query({
//                         model: "account.move",
//                         method: "action_open_due_date_wizard",
//                         args: [[recordId]],
//                     });
//                     console.log("Acción recibida:", action);
//                     this.env.bus.trigger("do-action", { action });
//                 });
//             });
//         },
//         willUnmount() {
//             this.el.querySelectorAll(".o_open_wizard_rpc_button").forEach((btn) => {
//                 btn.removeEventListener("click", this);
//             });
//             this._super(...arguments);
//         },
//     });
// }

// registry.category("addons").add("mod_prueba_tecnica_fac_patch", patchFormRenderer);
