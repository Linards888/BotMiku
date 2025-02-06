inputs = [1.2, 5.1, 2.1, 3.7]

weights = [[3.0, 2.7, 7.5, 1.1],
           [0.5, -2.0, 0, 0.1],
           [-0.26, 9, -2.2, 5.0]]

biases = [3, 1, 0.5]

bias1 = 3
bias2 = 1
bias3 = 0.5


layer_outputs = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)


print(layer_outputs)
