const { Component } = owl;
const { xml } = owl.tags;

export class CustomerList extends Component {
    static template = xml`
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Company</th>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                </tr>
            </thead>
            <tbody>
                <tr t-foreach="props.customers" t-as="customer">
                    <th scope="row"><t t-esc="customer.company_name" /></th>
                    <td><t t-esc="customer.first_name" /></td>
                    <td><t t-esc="customer.last_name" /></td>
                </tr>
            </tbody>
        </table>
    `;
}