const { Component } = owl;
const { xml } = owl.tags;

export class ContactForm extends Component {
    static template = xml /* xml */ `
        <div class="container">
            <div class="row" style="margin-top: 30px;">
                <h2>Contact Form</h2>
            </div>
        </div>
    `;
}