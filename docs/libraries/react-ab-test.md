# React A/B Test

* `<Experiment />` - Experiment container component
* `<Variant />` - 2 components inside an `<Experiment />`
*  `emitter` - responsible for coordinating and reporting usage

```jsx

import React from 'react';
import Experiment from 'react-ab-test/lib/Experiment';
import Variant from 'react-ab-test/lib/Variant';
import emitter from 'react-ab-test/lib/emitter';

export default class HelloWorld extends Component {

    onButtonClick(e) {
        this.experiment.win();
    }

    render() {
        return (
            <div>
                <Experiment
                    ref={(c) => { this.experiment = c; }}
                    name="My Example">
                    <Variant name="A">
                        <div>Section A</div>
                    </Variant>
                    <Variant name="B">
                        <div>Section B</div>
                    </Variant>
                </Experiment>
                <button onClick={this.onButtonClick.bind(this)}>
                    Emit a win
                </button>
            </div>
        );
    }
}

// Called when the experiment is displayed to the user.
emitter.addPlayListener(function(experimentName, variantName) {
    console.log(`Displaying experiment ‘${experimentName}’ variant ‘${variantName}’`);
});

// Called when a 'win' is emitted, in this case by this.experiment.win()
emitter.addWinListener(function(experimentName, variantName){
    console.log(`Variant ‘${variantName}’ experiment ‘${experimentName}’ was clicked`);
});
```

## Sources

* [react-ab-test Github](https://github.com/pushtell/react-ab-test)
* [How to quickly set up A/B testing for React websites](https://pillow.codes/how-to-quickly-set-up-a-b-testing-for-react-websites-dcb321fcd1f)