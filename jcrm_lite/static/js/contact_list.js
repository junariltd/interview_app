const { Component } = owl;
const { xml } = owl.tags;
const { Link } = owl.router;

export class ContactList extends Component {
    static components = { Link }
    static template = xml`
    <div class="container">
        <div class="row" style="margin-top: 30px;">
            <div class="col">
                <h2>Contacts</h2>
                <Link to="'CONTACT_FORM'" params="{id: 1}">Contact Form</Link>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Company</th>
                            <th scope="col">First Name</th>
                            <th scope="col">Last Name</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr t-foreach="[]" t-as="customer">
                            <th scope="row"><t t-esc="customer.company_name" /></th>
                            <td><t t-esc="customer.first_name" /></td>
                            <td><t t-esc="customer.last_name" /></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>`;
}