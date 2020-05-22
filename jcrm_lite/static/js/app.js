const { Component } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;

// Owl Components

class CustomerList extends Component {
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

class App extends Component {
    static components = { CustomerList }
    static template = xml`
        <div class="container">
            <div class="row" style="margin-top: 30px;">
                <h2>Customers</h2>
                <CustomerList customers="customers" />
            </div>
        </div>`;
    customers = [
        { company_name: 'ABC Customer Ltd', first_name: 'Mark', last_name: 'Otto' },
        { company_name: 'Dom\'s Doughnuts', first_name: 'Jacob', last_name: 'Thornton' },
        { company_name: 'Ed\'s Kebabs', first_name: 'Larry', last_name: 'the Bird' },
    ];
}

whenReady(() => {
    const app = new App();
    app.mount(document.getElementById('app'));
});
