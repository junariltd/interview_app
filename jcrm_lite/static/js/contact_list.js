const { Component, useState } = owl;
const { xml } = owl.tags;

export class ContactList extends Component {
    constructor() {
        super(...arguments);
        this.state = useState({
            loaded: false,
            contacts: []
        });
    }

    mounted() {
        this.loadContacts();
    }

    async loadContacts() {
        const contactsResponse = await fetch(this.env.apiPrefix + '/contacts');
        const contacts = await contactsResponse.json();
        this.state.loaded = true;
        this.state.contacts = contacts;
    }

    onRowClick(id) {
        this.env.router.navigate({
            to: 'contact_form', params: { id }
        });
    }

    static template = xml /* xml */ `
        <div class="container">
            <div class="row" style="margin-top: 30px;">
                <div class="col">
                    <h2>Contacts</h2>

                    <t t-if="state.loaded">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th scope="col">Company</th>
                                    <th scope="col">First Name</th>
                                    <th scope="col">Last Name</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr t-foreach="state.contacts" t-as="contact"
                                        t-on-click="onRowClick(contact.id)">
                                    <th scope="row"><t t-esc="contact.company_name" /></th>
                                    <td><t t-esc="contact.first_name" /></td>
                                    <td><t t-esc="contact.last_name" /></td>
                                </tr>
                            </tbody>
                        </table>
                    </t>
                </div>
            </div>
        </div>
    `;
}