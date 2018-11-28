# Scaling

* **Multivariate Testing** - each test not only has multiple cells, each cell has a slight different experience.
* **Conditional dependences** -
* The issue becomes scaling - for many experiences for many users, many different packages will have to be served

## Templating

```jsx
<div>
    <form>
        <input name='firstName' />
        <input name='lastName' />
        <input name='paypal' />
        <input name='cardNumber' />
        <input name='securityCode' />
        <select name='expirationMonth' />
        <select name='expirtaionYear' />
    </form>
</div>
```

* Bad idea to put all the conditional logic in the view, might get unsustainable


```jsx
<div>
    {condition1 ?
        <form>
            <input name='firstName' />
            <input name='lastName' />

        <input name='paypal' />
            <input name='cardNumber' />
            <input name='securityCode' />
            <select name='expirationMonth' />
            <select name='expirtaionYear' />
        </form>
        :null}
    {condition2 ?
        <form>
            <input name='firstName' />
            <input name='lastName' />
            <div>
                <input name='cardNumber' />
                <input name='securityCode' />
                <select name='expirationMonth' />
                <select name='expirtaionYear' />
            </div>
            <input name='paypal' />
        </form>
        :null}
    {condition1 ?
        <form>
            <input name='firstName' /><input name='lastName' />
            <input name='cardNumber' />
            <input name='securityCode' />
            <select name='expirationMonth' /><select name='expirtaionYear' />
        </form>
        :null}
</div>
```

* This is what we really want. And then some logic to handle what goes into `<PaymentMethod />`
* Flexible enough for all users, even those not in the test

```jsx
<div>
    <form>
        <input name='firstName' />
        <input name='lastName' />
        <PaymentMethod />
    </form>
</div>
```

* A rules engine
* Each rule evaluates to a template name
  * combine rules, as simple or complex as needed
  * by abstracting rules out to a separate file, improve template legibility
  * increases reuse: templates can be broken up and used anywhere

```json
[
    {
        "rules": [],
        "templateName": "control"
    },
    {
        "rules": ["Condition(2)"],
        "templateName": "payment-cell-2"
    },
    {
        "rules": ["Condition(3)"],
        "templateName": "payment-cell-3"
    },
    {
        "rules": ["Condition(2)", "Condition(3)"],
        "templateName": "payment-cell-4"
    },
]
```

### Packaging

* Try to make everything a module
  * true import export system
  * reduce globals
  * use static tools to build dependency trees
* A file may need different dependencies for testing.
  * If they are all bundled together, it can get large and cumbersome.
* why not ask things async?
  * pushes too much information and complexity to the client

```es6
// app.js

import oldSearch from 'old-search';
import newSearch from 'new-search';

export ...
```

* Problem is **Conditional Dependencies**
  * build a package specifically tailored to a user
    * don't force them to download files they don't need
    * don't force them to wait to download files they do need
* How do we know when a module is conditional?

```es6
// old-search.js
/*
 * @includewhen rule.notInNewSearch
 */

// new-search.js
/*
 * @includewhen rule.inNewSearch
 */
```


## Sources

* [Scaling A/B Testing on Netflix.com with Node.js](https://www.youtube.com/watch?v=VN4SNJ2JT9E)
* [Scaling A/B Testing on Netflix.com with Node.js](https://medium.com/netflix-techblog/scaling-a-b-testing-on-netflix-com-with-node-js-59e8101c00fc)
