pragma circom 2.0.0;
include "circomlib/circuits/poseidon.circom";
include "circomlib/circuits/comparators.circom";

template SATVerifier() {
    signal input score;      // SAT score  
    signal input threshold;
    signal output valid;     // 1 = success
    
    // verify score > threshold
    component comp = GreaterEqThan(11);
    comp.in[0] <== score;
    comp.in[1] <== threshold;

    valid <== comp.out;

}

component main = SATVerifier();
