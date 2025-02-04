inputs = [1.2, 5.1, 2.1, 3.7]

weights1 = [3.0, 2.7, 7.5, 1.1]
weights2 = [0.5, -2.0, 0, 0.1]
weights3 = [-0.26, 9, -2.2, 5.0]

bias1 = 3
bias2 = 1
bias3 = 0.5

output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]
print(output)