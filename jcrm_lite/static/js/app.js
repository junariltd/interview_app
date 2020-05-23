import { CustomerList } from '/static/js/customer_list.js';

const { Component } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;

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
