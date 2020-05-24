import { ContactList } from '/static/js/contact_list.js';
import { ContactForm } from '/static/js/contact_form.js';

const { Component } = owl;
const { xml } = owl.tags;
const { Router, RouteComponent } = owl.router;
const { whenReady } = owl.utils;

class App extends Component {
    static components = { RouteComponent }
    static template = xml`
        <RouteComponent />
    `;
}

const ROUTES = [
    { name: "CONTACT_LIST", path: "/", component: ContactList },
    { name: "CONTACT_FORM", path: "/contacts/{{id}}", component: ContactForm },
];

whenReady(async () => {
    const app = new App();
    app.env.apiPrefix = '/api/v1';
    app.env.router = new Router(app.env, ROUTES);
    await app.env.router.start();
    app.mount(document.getElementById('app'));
});
