def warmup_decay_schedule(base_lr, warmup_steps, total_steps, current_step):
    if current_step < warmup_steps:
        lr = base_lr*(current_step/warmup_steps)
    elif current_step > warmup_steps: 
        lr = base_lr*((total_steps - current_step)/(total_steps -warmup_steps))
    else: 
        lr = base_lr
    return lr