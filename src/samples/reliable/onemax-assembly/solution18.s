    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-19079, %eax
    movl	$24213, %ebx
    movl	$26675, %ecx
    movl	$-10947, %edx

    shl $7, %ebx
    shr $60, %edx
    sub %ebx, %edx
    shr $164, %ecx
    shl $238, %ecx
    and %ecx, %ecx
    jno n41
    shl $50, %edx
    and %ebx, %ecx
    and %edx, %eax
    shr $74, %eax
    jne n41
    and %ebx, %ebx
    shl $117, %edx
    xor %ebx, %edx
    jno n39
    shl $131, %edx
    shl $235, %ebx
    jc n27
    jnz n46
    xor %edx, %ebx
    shr $17, %eax
    cmp %eax, %eax
    shl $70, %ebx
n27:
    add %ebx, %eax
    shr $233, %ecx
    ja n45
    cmp %edx, %eax
    shr $210, %eax
    shr $140, %ecx
    add %edx, %ebx
    jz n36
    jno n38
n36:
    sub %ebx, %ecx
    and %ecx, %edx
n38:
    shr $191, %edx
n39:
    shl $124, %ebx
    jne n42
n41:
    ja n42
n42:
    jnc n46
    or %edx, %eax
    cmp %eax, %ebx
n45:
    add %edx, %edx
n46:
    jc n47
n47:
    jno n48
n48:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
