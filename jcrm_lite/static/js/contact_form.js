const { Component, useState } = owl;
const { Link } = owl.router;
const { xml } = owl.tags;

export class ContactForm extends Component {

    constructor() {
        super(...arguments);
        this.state = useState({
            loaded: false,
            contact: {}
        });
    }

    mounted() {
        this.loadContact();
    }

    async loadContact() {
        const contactResponse = await fetch(this.env.apiPrefix + '/contact/' + this.props.id);
        const contact = await contactResponse.json();
        this.state.loaded = true;
        this.state.contact = contact;
    }

    async saveContact(e) {
        e.preventDefault();
        const { company_name, first_name, last_name } = this.state.contact
        const contact_update = {
            company_name, first_name, last_name
        }
        const updateResponse = await fetch(this.env.apiPrefix + '/contact/' + this.props.id, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(contact_update)
        })
        const updateResult = await updateResponse.json()
        if (updateResult.success) {
            this.env.router.navigate({ to: 'contact_list' });
        }
        else {
            throw new Error('Contact Update Unsuccessful: ' + JSON.stringify(updateResult))
        }
    }

    static components = { Link };
    static template = xml /* xml */ `
        <div class="container">
            <div class="row" style="margin-top: 30px;">
                <div class="col">
                    <h2>Edit Contact</h2>
                    <p><Link to="'contact_list'">&lt; Back to List</Link></p>

                    <t t-if="state.loaded">
                        <form>
                            <div class="form-group row">
                                <label for="company_name" class="col-sm-2 col-form-label">Company Name</label>
                                <div class="col-sm-10">
                                    <input type="text" class="form-control" name="company_name" t-model="state.contact.company_name" />
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="first_name" class="col-sm-2 col-form-label">First Name</label>
                                <div class="col-sm-10">
                                    <input type="text" class="form-control" name="first_name" t-model="state.contact.first_name" />
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="last_name" class="col-sm-2 col-form-label">Last Name</label>
                                <div class="col-sm-10">
                                    <input type="text" class="form-control" name="last_name" t-model="state.contact.last_name" />
                                </div>
                            </div>
                            <button class="btn btn-primary" type="submit"
                                t-on-click="saveContact">Save Changes</button>
                        </form>
                    </t>

                </div>
            </div>
        </div>
    `;
}