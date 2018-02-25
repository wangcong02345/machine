function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
 
for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

    h_theta =  X * theta;
    loss = h_theta - y;
    
    no_sum0 = loss'*X(:,1);
    sum0 = sum(no_sum0);
    theta(1,1) = theta(1,1) - alpha * (1/m) * sum0;
    
    no_sum1 = loss'*X(:,2);
    sum1 = sum(no_sum1);
    theta(2,1) = theta(2,1) - alpha * (1/m) * sum1;
    %fprintf ("theta0=%f,theta1=%f", theta0, theta1);

    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

end
